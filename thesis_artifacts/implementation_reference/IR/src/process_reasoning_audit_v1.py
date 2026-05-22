"""process_reasoning_audit_v1.py

Deterministic reasoning probes for the DZ process/workflow layer.

This audit validates the process files as a graph and grounding envelope. It
does not rewrite A4V3 files and does not replace local IR, bridge, canonical
ontology, or provenance.

CLI:
    python IR/src/process_reasoning_audit_v1.py --dz-root IR/outputs/runs/dz
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

THIS_DIR = Path(__file__).resolve().parent
if str(THIS_DIR) not in sys.path:
    sys.path.insert(0, str(THIS_DIR))

from a4v3_parser_v1 import parse  # noqa: E402


PROCESS_FILES = [
    "process_ontology_v1.a4v3",
    "ordinary_rebalance_workflow_v1.a4v3",
    "exception_overlays_v1.a4v3",
]

CALL_RE = re.compile(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(([^()]*)\)")

WORKFLOW_RELATIONS = {
    "workflow_step",
    "workflow_invokes",
    "workflow_modifies",
    "workflow_interrupts",
}

GROUNDING_RELATIONS = {
    "grounding_document_part",
    "grounding_source_fragment",
    "grounding_bridge_family",
    "grounding_bridge_decision",
    "grounding_canonical_concept",
    "grounding_canonical_frame",
    "grounding_local_assertion",
    "grounding_provenance_claim",
}

ALLOWED_TERMINAL_STEPS = {
    "ImplementOrdinaryRebalance",
    "ImplementCorporateActionAdjustment",
    "DetermineIndexUnderDisruptedConditions",
    "CorrectIdentifiedError",
    "AnnounceIndexTermination",
    "AnnounceMethodologyChange",
    "UpdateGuidelineAmendmentDate",
    "EnsureConsistentCalculationMethodAfterChange",
    "MakeApprovedRuleOrGuidelineAmendment",
}

TERMINAL_STATE_NAMES = {
    "TerminatedIndexState",
    "CorrectionResolvedState",
    "CorporateActionAdjustedComponentState",
    "MethodologyChangedState",
    "AmendmentApprovedState",
    "ImplementedComponentState",
    "DisruptedDeterminationState",
}

TERMINAL_OUTPUT_NAME_PARTS = (
    "Terminated",
    "Corrected",
    "Approved",
    "Implemented",
    "Consistent",
    "Disrupted",
    "Updated",
    "Announcement",
)

EXTERNAL_INPUT_NAME_PARTS = (
    "Event",
    "Component",
    "Kind",
    "Price",
    "Policy",
    "Methodology",
    "Notice",
    "Error",
    "Calculation",
    "Review",
    "Amendment",
    "Committee",
    "Universe",
    "Selected",
    "Weights",
    "Shares",
    "Capitalization",
    "Changes",
)


def _split_args(raw: str) -> list[str]:
    return [arg.strip() for arg in raw.split(",") if arg.strip()]


def _calls_from_assertions(ast: dict[str, Any], file_name: str) -> list[dict[str, Any]]:
    calls: list[dict[str, Any]] = []
    for decl in ast.get("assertions", []):
        raw = decl.get("raw") or ""
        for match in CALL_RE.finditer(raw):
            calls.append(
                {
                    "rel": match.group(1),
                    "args": _split_args(match.group(2)),
                    "assertion": decl.get("name"),
                    "file": file_name,
                    "line_no": decl.get("line_no"),
                }
            )
    return calls


def _declared_entities(ast: dict[str, Any], sort_name: str) -> set[str]:
    out: set[str] = set()
    for decl in ast.get("declarations", []):
        if decl.get("family") == "SymbolDecl" and decl.get("kind") == "entity":
            if decl.get("sort") == sort_name:
                out.add(decl.get("name", ""))
    return {x for x in out if x}


def _call_set(calls: list[dict[str, Any]], rel: str, arity: int | None = None) -> set[tuple[str, ...]]:
    out: set[tuple[str, ...]] = set()
    for call in calls:
        if call["rel"] != rel:
            continue
        if arity is not None and len(call["args"]) != arity:
            continue
        out.add(tuple(call["args"]))
    return out


def _call_map(calls: list[dict[str, Any]], rel: str) -> dict[tuple[str, ...], list[dict[str, Any]]]:
    out: dict[tuple[str, ...], list[dict[str, Any]]] = defaultdict(list)
    for call in calls:
        if call["rel"] == rel:
            out[tuple(call["args"])].append(call)
    return out


def _finding(
    code: str,
    severity: str,
    message: str,
    *,
    file: str | None = None,
    data: dict[str, Any] | None = None,
) -> dict[str, Any]:
    item: dict[str, Any] = {"code": code, "severity": severity, "message": message}
    if file:
        item["file"] = file
    if data:
        item["data"] = data
    return item


def _has_name_part(name: str, parts: tuple[str, ...]) -> bool:
    return any(part in name for part in parts)


def _workflow_graph(workflows: set[str], workflow_steps: set[tuple[str, str]], edges: set[tuple[str, str]]) -> dict[str, Any]:
    steps_by_workflow: dict[str, set[str]] = {w: set() for w in workflows}
    for workflow, step in workflow_steps:
        steps_by_workflow.setdefault(workflow, set()).add(step)

    graph: dict[str, Any] = {}
    for workflow, steps in steps_by_workflow.items():
        incoming: dict[str, set[str]] = {s: set() for s in steps}
        outgoing: dict[str, set[str]] = {s: set() for s in steps}
        for a, b in edges:
            if a in steps and b in steps:
                outgoing[a].add(b)
                incoming[b].add(a)
        graph[workflow] = {"steps": steps, "incoming": incoming, "outgoing": outgoing}
    return graph


def _is_external_input(input_name: str, input_kinds: dict[str, set[str]]) -> bool:
    kinds = input_kinds.get(input_name, set())
    if {"DomainConceptIO", "ObservationFrameIO", "CalendarMarkerIO"} & kinds:
        return True
    if "ProcessStateIO" in kinds and _has_name_part(input_name, EXTERNAL_INPUT_NAME_PARTS):
        return True
    return _has_name_part(input_name, EXTERNAL_INPUT_NAME_PARTS)


def analyze(dz_root: Path) -> dict[str, Any]:
    process_dir = dz_root / "process"
    findings: list[dict[str, Any]] = []
    asts: dict[str, dict[str, Any]] = {}
    all_calls: list[dict[str, Any]] = []
    process_files: list[str] = []

    for name in PROCESS_FILES:
        path = process_dir / name
        if not path.exists():
            findings.append(
                _finding(
                    "process_file_missing",
                    "hard",
                    f"Required process file {name} is missing.",
                    file=name,
                    data={"path": str(path)},
                )
            )
            continue
        process_files.append(name)
        text = path.read_text(encoding="utf-8")
        ast = parse(text, strict=False)
        asts[name] = ast
        if ast.get("warnings"):
            findings.append(
                _finding(
                    "process_parse_warnings",
                    "hard",
                    f"Process file {name} has parser warnings.",
                    file=name,
                    data={"warnings": ast.get("warnings", [])[:20]},
                )
            )
        all_calls.extend(_calls_from_assertions(ast, name))

    process_steps: set[str] = set()
    workflows: set[str] = set()
    grounding_targets: set[str] = set()
    for name, ast in asts.items():
        process_steps |= _declared_entities(ast, "ProcessStep")
        workflows |= _declared_entities(ast, "Workflow")
        grounding_targets |= _declared_entities(ast, "ProcessGroundingTarget")

    workflow_steps = _call_set(all_calls, "workflow_step", 2)
    step_to_workflows: dict[str, set[str]] = defaultdict(set)
    for workflow, step in workflow_steps:
        step_to_workflows[step].add(workflow)

    step_grounded = {args[0] for args in _call_set(all_calls, "step_grounded_in", 2)}
    step_modality = {args[0] for args in _call_set(all_calls, "step_modality", 2)}
    step_iteration = {args[0] for args in _call_set(all_calls, "step_iteration_status", 2)}
    step_overlay_behavior = {args[0] for args in _call_set(all_calls, "step_overlay_behavior", 2)}

    ordinary_workflow = "OrdinaryRebalanceWorkflow"
    overlay_steps = {step for step, wfs in step_to_workflows.items() if ordinary_workflow not in wfs}

    for step in sorted(process_steps):
        if step not in step_to_workflows:
            findings.append(
                _finding(
                    "process_step_without_workflow",
                    "hard",
                    f"ProcessStep {step} is not attached to any workflow_step.",
                    data={"step": step},
                )
            )
        if step not in step_grounded:
            findings.append(
                _finding(
                    "process_step_without_grounding",
                    "hard",
                    f"ProcessStep {step} has no step_grounded_in relation.",
                    data={"step": step},
                )
            )
        if step not in step_modality:
            findings.append(
                _finding(
                    "process_step_without_modality",
                    "hard",
                    f"ProcessStep {step} has no step_modality relation.",
                    data={"step": step},
                )
            )
        if step not in step_iteration:
            findings.append(
                _finding(
                    "process_step_without_iteration_status",
                    "hard",
                    f"ProcessStep {step} has no step_iteration_status relation.",
                    data={"step": step},
                )
            )
        if step in overlay_steps and step not in step_overlay_behavior:
            findings.append(
                _finding(
                    "overlay_step_without_behavior",
                    "hard",
                    f"Overlay ProcessStep {step} has no step_overlay_behavior relation.",
                    data={"step": step},
                )
            )

    edges = _call_set(all_calls, "step_precedes", 2)
    edge_kinds = _call_set(all_calls, "step_edge_kind", 3)
    edge_temporal = _call_set(all_calls, "step_temporal_relation", 3)
    edge_grounding = _call_set(all_calls, "edge_grounded_in", 3)
    edge_kind_prefixes = {(a, b) for a, b, _kind in edge_kinds}
    edge_temporal_prefixes = {(a, b) for a, b, _rel in edge_temporal}
    edge_grounding_prefixes = {(a, b) for a, b, _grounding in edge_grounding}

    for a, b in sorted(edges):
        if (a, b) not in edge_kind_prefixes:
            findings.append(
                _finding(
                    "edge_without_kind",
                    "hard",
                    f"step_precedes({a}, {b}) has no step_edge_kind.",
                    data={"from": a, "to": b},
                )
            )
        if (a, b) not in edge_temporal_prefixes:
            findings.append(
                _finding(
                    "edge_without_temporal_relation",
                    "hard",
                    f"step_precedes({a}, {b}) has no step_temporal_relation.",
                    data={"from": a, "to": b},
                )
            )
        if (a, b) not in edge_grounding_prefixes:
            findings.append(
                _finding(
                    "edge_without_grounding",
                    "hard",
                    f"step_precedes({a}, {b}) has no edge_grounded_in.",
                    data={"from": a, "to": b},
                )
            )

    inferred_edges = [(a, b) for a, b, kind in edge_kinds if kind == "InferredMergeEdge"]
    for a, b in inferred_edges:
        findings.append(
            _finding(
                "inferred_merge_edge_requires_review",
                "soft",
                f"step_edge_kind({a}, {b}, InferredMergeEdge) requires explicit review notes.",
                data={"from": a, "to": b},
            )
        )

    graph = _workflow_graph(workflows, workflow_steps, edges)
    for workflow in sorted(workflows):
        data = graph.get(workflow, {"steps": set(), "incoming": {}, "outgoing": {}})
        steps = data["steps"]
        if not steps:
            findings.append(
                _finding(
                    "workflow_without_steps",
                    "hard",
                    f"Workflow {workflow} has no workflow_step entries.",
                    data={"workflow": workflow},
                )
            )
            continue
        starts = sorted(step for step in steps if not data["incoming"].get(step))
        if len(starts) > 1:
            findings.append(
                _finding(
                    "workflow_multiple_start_steps",
                    "soft",
                    f"Workflow {workflow} has multiple start steps.",
                    data={"workflow": workflow, "starts": starts},
                )
            )
        for step in sorted(steps):
            if data["incoming"].get(step):
                continue
            if step in starts:
                continue
            findings.append(
                _finding(
                    "non_start_step_without_incoming_edge",
                    "hard",
                    f"Step {step} in {workflow} has no incoming edge.",
                    data={"workflow": workflow, "step": step},
                )
            )
        for step in sorted(steps):
            if data["outgoing"].get(step):
                continue
            produced_outputs = [out for s, out in _call_set(all_calls, "step_produces", 2) if s == step]
            entered_states = [state for s, state in _call_set(all_calls, "step_enters_state", 2) if s == step]
            terminalish = (
                step in ALLOWED_TERMINAL_STEPS
                or any(state in TERMINAL_STATE_NAMES for state in entered_states)
                or any(_has_name_part(out, TERMINAL_OUTPUT_NAME_PARTS) for out in produced_outputs)
            )
            if not terminalish:
                findings.append(
                    _finding(
                        "non_terminal_step_without_outgoing_edge",
                        "soft",
                        f"Step {step} in {workflow} has no outgoing edge and is not recognized as terminal.",
                        data={
                            "workflow": workflow,
                            "step": step,
                            "produced_outputs": produced_outputs,
                            "entered_states": entered_states,
                        },
                    )
                )

    input_kinds: dict[str, set[str]] = defaultdict(set)
    for input_name, kind in _call_set(all_calls, "input_kind", 2):
        input_kinds[input_name].add(kind)
    output_kinds: dict[str, set[str]] = defaultdict(set)
    for output_name, kind in _call_set(all_calls, "output_kind", 2):
        output_kinds[output_name].add(kind)

    required_inputs = _call_set(all_calls, "step_requires", 2)
    produced_outputs = _call_set(all_calls, "step_produces", 2)
    produced_names = {out for _step, out in produced_outputs}
    for step, input_name in sorted(required_inputs):
        if input_name not in input_kinds:
            findings.append(
                _finding(
                    "input_without_input_kind",
                    "hard",
                    f"Input {input_name} required by {step} has no input_kind.",
                    data={"step": step, "input": input_name},
                )
            )
        if input_name not in produced_names and _is_external_input(input_name, input_kinds):
            findings.append(
                _finding(
                    "external_input_accepted",
                    "advisory",
                    f"Input {input_name} required by {step} is accepted as external/source-backed.",
                    data={"step": step, "input": input_name, "input_kinds": sorted(input_kinds.get(input_name, []))},
                )
            )
        elif input_name not in produced_names:
            findings.append(
                _finding(
                    "unproduced_input_requires_review",
                    "soft",
                    f"Input {input_name} required by {step} is not produced by an earlier process output.",
                    data={"step": step, "input": input_name, "input_kinds": sorted(input_kinds.get(input_name, []))},
                )
            )
    for step, output_name in sorted(produced_outputs):
        if output_name not in output_kinds:
            findings.append(
                _finding(
                    "output_without_output_kind",
                    "hard",
                    f"Output {output_name} produced by {step} has no output_kind.",
                    data={"step": step, "output": output_name},
                )
            )

    # Overlay behavior semantic probes.
    behavior_by_step: dict[str, set[str]] = defaultdict(set)
    for step, behavior in _call_set(all_calls, "step_overlay_behavior", 2):
        behavior_by_step[step].add(behavior)
    state_entries = _call_set(all_calls, "step_enters_state", 2)
    state_exits = _call_set(all_calls, "step_exits_state", 2)
    outputs_by_step: dict[str, set[str]] = defaultdict(set)
    for step, output_name in produced_outputs:
        outputs_by_step[step].add(output_name)

    for step, behaviors in sorted(behavior_by_step.items()):
        entered = {state for s, state in state_entries if s == step}
        outputs = outputs_by_step.get(step, set())
        if "Fallback" in behaviors and not outputs and not entered:
            findings.append(
                _finding(
                    "fallback_step_without_output",
                    "soft",
                    f"Fallback step {step} does not produce an output or enter a state.",
                    data={"step": step},
                )
            )
        if "ModifyAndContinue" in behaviors:
            names = set(outputs) | set(entered)
            if not any(
                part in name
                for name in names
                for part in ("Adjust", "Changed", "Disrupt", "Arrangement", "Announcement", "Consistent", "Guideline")
            ):
                findings.append(
                    _finding(
                        "modify_continue_without_adjusted_artifact",
                        "advisory",
                        f"ModifyAndContinue step {step} has no obviously adjusted/changed output or state.",
                        data={"step": step, "entered_states": sorted(entered), "outputs": sorted(outputs)},
                    )
                )

    for workflow, data in sorted(graph.items()):
        steps = data["steps"]
        workflow_behaviors = {behavior for step in steps for behavior in behavior_by_step.get(step, set())}
        workflow_entered = {state for step, state in state_entries if step in steps}
        workflow_exited = {state for step, state in state_exits if step in steps}
        workflow_outputs = {out for step, out in produced_outputs if step in steps}
        if "Preempt" in workflow_behaviors:
            if not (workflow_entered & TERMINAL_STATE_NAMES or any("Terminated" in out for out in workflow_outputs)):
                findings.append(
                    _finding(
                        "preempt_workflow_without_terminal_state",
                        "soft",
                        f"Preempt workflow {workflow} does not enter a recognized terminal state or output.",
                        data={
                            "workflow": workflow,
                            "entered_states": sorted(workflow_entered),
                            "outputs": sorted(workflow_outputs),
                        },
                    )
                )
        if "InterruptAndResume" in workflow_behaviors:
            names = workflow_entered | workflow_outputs
            has_resume_marker = bool(workflow_exited) or any(
                part in name
                for name in names
                for part in ("Resolved", "Approved", "Corrected", "AmendmentApproved")
            )
            if not has_resume_marker:
                findings.append(
                    _finding(
                        "interrupt_resume_workflow_without_lifecycle_marker",
                        "soft",
                        f"InterruptAndResume workflow {workflow} has no state exit, resolved/approved state, or output.",
                        data={
                            "workflow": workflow,
                            "entered_states": sorted(workflow_entered),
                            "exited_states": sorted(workflow_exited),
                            "outputs": sorted(workflow_outputs),
                        },
                    )
                )

    grounding_kind = {args[0] for args in _call_set(all_calls, "grounding_kind", 2)}
    concrete_grounded_targets: set[str] = set()
    for rel in GROUNDING_RELATIONS:
        concrete_grounded_targets |= {args[0] for args in _call_set(all_calls, rel)}
    for target in sorted(grounding_targets):
        if target not in grounding_kind:
            findings.append(
                _finding(
                    "grounding_target_without_kind",
                    "hard",
                    f"Grounding target {target} has no grounding_kind.",
                    data={"grounding_target": target},
                )
            )
        if target not in concrete_grounded_targets:
            findings.append(
                _finding(
                    "grounding_target_without_concrete_grounding",
                    "hard",
                    f"Grounding target {target} has no concrete grounding relation.",
                    data={"grounding_target": target},
                )
            )
    bridge_grounding_targets = {target for target, kind in _call_set(all_calls, "grounding_kind", 2) if kind == "BridgeDecisionGrounding"}
    bridge_family_targets = {args[0] for args in _call_set(all_calls, "grounding_bridge_family", 2)}
    for target in sorted(bridge_grounding_targets - bridge_family_targets):
        findings.append(
            _finding(
                "bridge_grounding_without_bridge_family",
                "hard",
                f"Bridge grounding target {target} has no grounding_bridge_family.",
                data={"grounding_target": target},
            )
        )
    trigger_relations = _call_set(all_calls, "trigger_temporal_relation", 3)
    trigger_relation_grounded = {(a, b) for a, b, _target in _call_set(all_calls, "trigger_relation_grounded_in", 3)}
    for a, b, relation in sorted(trigger_relations):
        if relation in {"Before", "SameTimeAs"} and (a, b) not in trigger_relation_grounded:
            severity = "advisory"
            findings.append(
                _finding(
                    "trigger_temporal_relation_without_grounding",
                    severity,
                    f"trigger_temporal_relation({a}, {b}, {relation}) has no trigger_relation_grounded_in.",
                    data={"from": a, "to": b, "relation": relation},
                )
            )

    severity_counts = Counter(f["severity"] for f in findings)
    status = "blocked" if severity_counts.get("hard", 0) else "passed_with_review_items"
    if not findings:
        status = "passed"

    return {
        "schema": "process_reasoning_audit_v1",
        "dz_root": str(dz_root),
        "process_files": process_files,
        "process_step_count": len(process_steps),
        "workflow_count": len(workflows),
        "step_edge_count": len(edges),
        "grounding_target_count": len(grounding_targets),
        "findings": findings,
        "hard_findings": severity_counts.get("hard", 0),
        "soft_findings": severity_counts.get("soft", 0),
        "advisory_findings": severity_counts.get("advisory", 0),
        "status": status,
    }


def _write_markdown(report: dict[str, Any], out_path: Path) -> None:
    lines: list[str] = []
    lines.append("# Process Reasoning Audit v1")
    lines.append("")
    lines.append(f"Status: `{report['status']}`")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    for key in [
        "process_step_count",
        "workflow_count",
        "step_edge_count",
        "grounding_target_count",
        "hard_findings",
        "soft_findings",
        "advisory_findings",
    ]:
        lines.append(f"- `{key}`: {report.get(key)}")
    lines.append("")
    lines.append("## Findings")
    lines.append("")
    findings = report.get("findings", [])
    if not findings:
        lines.append("No findings.")
    else:
        for i, finding in enumerate(findings, start=1):
            file_part = f" file `{finding['file']}`" if finding.get("file") else ""
            lines.append(f"{i}. `{finding['severity']}` `{finding['code']}`{file_part}: {finding['message']}")
            data = finding.get("data") or {}
            compact = {
                k: data[k]
                for k in (
                    "workflow",
                    "step",
                    "from",
                    "to",
                    "input",
                    "output",
                    "grounding_target",
                    "relation",
                    "input_kinds",
                )
                if k in data
            }
            if compact:
                lines.append(f"   Data: `{json.dumps(compact, ensure_ascii=False)}`")
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    lines.append(
        "Hard findings block process-layer readiness. Soft findings require an "
        "explicit modeling decision or note. Advisory findings document accepted "
        "external inputs, intentional deferrals, or useful review prompts."
    )
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dz-root", default="IR/outputs/runs/dz")
    ap.add_argument("--out-dir", default=None)
    args = ap.parse_args()

    dz_root = Path(args.dz_root)
    out_dir = Path(args.out_dir) if args.out_dir else dz_root / "reasoning"
    out_dir.mkdir(parents=True, exist_ok=True)

    report = analyze(dz_root)
    json_path = out_dir / "process_reasoning_audit_v1.json"
    md_path = out_dir / "process_reasoning_audit_v1.md"
    json_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    _write_markdown(report, md_path)
    print(
        json.dumps(
            {
                "status": report["status"],
                "hard_findings": report["hard_findings"],
                "soft_findings": report["soft_findings"],
                "advisory_findings": report["advisory_findings"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
