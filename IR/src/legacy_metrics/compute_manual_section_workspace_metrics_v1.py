"""Minimal A4V3 expression parser compatibility module.

The full research repository historically reused this module from a larger
legacy metrics package. The public release keeps only the small expression
parser surface needed by ``a4v3_parser_v1``:

* ``ExprParser``
* ``IrParseError``
* ``_split_top_level``

No LLM calls, dotenv loading, workspace paths, or experiment-specific metrics
are included here.
"""
from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any


def _split_top_level(text: str, sep: str = ",") -> list[str]:
    """Split ``text`` by ``sep`` while respecting parentheses."""
    parts: list[str] = []
    current: list[str] = []
    depth = 0
    for ch in text:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        if ch == sep and depth == 0:
            piece = "".join(current).strip()
            if piece:
                parts.append(piece)
            current = []
            continue
        current.append(ch)
    tail = "".join(current).strip()
    if tail:
        parts.append(tail)
    return parts


@dataclass(frozen=True)
class Token:
    kind: str
    value: str


class IrParseError(RuntimeError):
    """Raised when an A4V3 expression cannot be parsed."""


class ExprParser:
    """Small recursive-descent parser for the A4V3 expression subset."""

    def __init__(self, text: str) -> None:
        self.tokens = self._tokenize(text)
        self.pos = 0

    @staticmethod
    def _tokenize(text: str) -> list[Token]:
        token_re = re.compile(
            r"""
            (?P<WS>\s+)
          | (?P<ARROW>->)
          | (?P<NE>!=)
          | (?P<LE><=)
          | (?P<GE>>=)
          | (?P<LT><)
          | (?P<GT>>)
          | (?P<LPAREN>\()
          | (?P<RPAREN>\))
          | (?P<COMMA>,)
          | (?P<DOT>\.)
          | (?P<COLON>:)
          | (?P<EQ>=)
          | (?P<STAR>\*)
          | (?P<SLASH>/)
          | (?P<PLUS>\+)
          | (?P<MINUS>-)
          | (?P<NUMBER>\d+(?:\.\d+)?%?)
          | (?P<IDENT>[A-Za-z_][A-Za-z0-9_]*)
            """,
            re.VERBOSE,
        )
        pos = 0
        tokens: list[Token] = []
        while pos < len(text):
            match = token_re.match(text, pos)
            if not match:
                raise IrParseError(f"Unexpected token near: {text[pos:pos+60]!r}")
            pos = match.end()
            kind = match.lastgroup or ""
            value = match.group()
            if kind != "WS":
                tokens.append(Token(kind, value))
        return tokens

    def _peek(self, offset: int = 0) -> Token | None:
        idx = self.pos + offset
        if 0 <= idx < len(self.tokens):
            return self.tokens[idx]
        return None

    def _match(self, *, kind: str | None = None, value: str | None = None) -> Token | None:
        token = self._peek()
        if token is None:
            return None
        if kind is not None and token.kind != kind:
            return None
        if value is not None and token.value != value:
            return None
        self.pos += 1
        return token

    def _expect(self, *, kind: str | None = None, value: str | None = None) -> Token:
        token = self._match(kind=kind, value=value)
        if token is None:
            got = self._peek()
            raise IrParseError(
                f"Expected {kind or value}, got {got.value if got else 'EOF'}"
            )
        return token

    def parse(self) -> dict[str, Any]:
        expr = self._parse_expr()
        if self._peek() is not None:
            trailing = self._peek()
            raise IrParseError(f"Unexpected trailing token {trailing.value!r}")
        return expr

    def _parse_expr(self) -> dict[str, Any]:
        token = self._peek()
        if token and token.kind == "IDENT" and token.value in {"forall", "exists"}:
            return self._parse_quantifier()
        return self._parse_implies()

    def _parse_quantifier(self) -> dict[str, Any]:
        kind = self._expect(kind="IDENT").value
        vars_payload: list[dict[str, str]] = []
        while True:
            name = self._expect(kind="IDENT").value
            self._expect(kind="COLON")
            sort = self._expect(kind="IDENT").value
            vars_payload.append({"name": name, "sort": sort})
            if self._match(kind="DOT"):
                return {"kind": kind, "vars": vars_payload, "body": self._parse_expr()}
            self._expect(kind="COMMA")
            if (
                self._peek()
                and self._peek().kind == "IDENT"
                and self._peek(1)
                and self._peek(1).kind == "COLON"
            ):
                continue
            return {"kind": kind, "vars": vars_payload, "body": self._parse_expr()}

    def _parse_implies(self) -> dict[str, Any]:
        left = self._parse_or()
        token = self._peek()
        if token and token.kind == "IDENT" and token.value in {"implies", "iff"}:
            op = self._expect(kind="IDENT").value
            return {"kind": op, "left": left, "right": self._parse_implies()}
        return left

    def _parse_or(self) -> dict[str, Any]:
        args = [self._parse_and()]
        while self._peek() and self._peek().kind == "IDENT" and self._peek().value == "or":
            self._expect(kind="IDENT")
            args.append(self._parse_and())
        if len(args) == 1:
            return args[0]
        return {"kind": "or", "args": self._flatten("or", args)}

    def _parse_and(self) -> dict[str, Any]:
        args = [self._parse_not()]
        while self._peek() and self._peek().kind == "IDENT" and self._peek().value == "and":
            self._expect(kind="IDENT")
            args.append(self._parse_not())
        if len(args) == 1:
            return args[0]
        return {"kind": "and", "args": self._flatten("and", args)}

    @staticmethod
    def _flatten(kind: str, args: list[dict[str, Any]]) -> list[dict[str, Any]]:
        out: list[dict[str, Any]] = []
        for item in args:
            if isinstance(item, dict) and item.get("kind") == kind:
                out.extend(item.get("args", []))
            else:
                out.append(item)
        return out

    def _parse_not(self) -> dict[str, Any]:
        token = self._peek()
        if token and token.kind == "IDENT" and token.value == "not":
            self._expect(kind="IDENT")
            return {"kind": "not", "arg": self._parse_not()}
        return self._parse_compare()

    def _parse_compare(self) -> dict[str, Any]:
        left = self._parse_addsub()
        token = self._peek()
        if token is None:
            return left
        mapping = {"EQ": "eq", "LE": "lte", "GE": "gte", "LT": "lt", "GT": "gt"}
        if token.kind == "NE":
            self.pos += 1
            return {
                "kind": "not",
                "arg": {"kind": "eq", "left": left, "right": self._parse_addsub()},
            }
        if token.kind == "IDENT" and token.value == "isa":
            self.pos += 1
            return {"kind": "isa", "expr": left, "sort": self._expect(kind="IDENT").value}
        if token.kind in mapping:
            self.pos += 1
            return {"kind": mapping[token.kind], "left": left, "right": self._parse_addsub()}
        return left

    def _parse_addsub(self) -> dict[str, Any]:
        left = self._parse_muldiv()
        while True:
            token = self._peek()
            if token is None or token.kind not in {"PLUS", "MINUS"}:
                return left
            self.pos += 1
            right = self._parse_muldiv()
            left = {
                "kind": "add" if token.kind == "PLUS" else "sub",
                "left": left,
                "right": right,
            }

    def _parse_muldiv(self) -> dict[str, Any]:
        left = self._parse_primary()
        while True:
            token = self._peek()
            if token is None or token.kind not in {"STAR", "SLASH"}:
                return left
            self.pos += 1
            right = self._parse_primary()
            left = {
                "kind": "mul" if token.kind == "STAR" else "div",
                "left": left,
                "right": right,
            }

    def _parse_primary(self) -> dict[str, Any]:
        if self._match(kind="LPAREN"):
            expr = self._parse_expr()
            self._expect(kind="RPAREN")
            return expr
        token = self._peek()
        if token is None:
            raise IrParseError("Unexpected EOF while parsing expression")
        if token.kind == "NUMBER":
            return {"kind": "ref", "name": self._expect(kind="NUMBER").value}
        if token.kind != "IDENT":
            raise IrParseError(f"Unexpected token {token.value!r}")
        name = self._expect(kind="IDENT").value
        if name == "ite":
            self._expect(kind="LPAREN")
            cond = self._parse_expr()
            self._expect(kind="COMMA")
            then_expr = self._parse_expr()
            self._expect(kind="COMMA")
            else_expr = self._parse_expr()
            self._expect(kind="RPAREN")
            return {"kind": "ite", "cond": cond, "then": then_expr, "else": else_expr}
        if name in {"count", "sum"}:
            return self._parse_aggregate(name)
        if self._match(kind="LPAREN"):
            args: list[dict[str, Any]] = []
            if not self._match(kind="RPAREN"):
                while True:
                    args.append(self._parse_expr())
                    if self._match(kind="COMMA"):
                        continue
                    self._expect(kind="RPAREN")
                    break
            return {"kind": "call", "callee": name, "args": args}
        return {"kind": "ref", "name": name}

    def _parse_aggregate(self, name: str) -> dict[str, Any]:
        self._expect(kind="LPAREN")
        binder_name = self._expect(kind="IDENT").value
        self._expect(kind="IDENT", value="in")
        binder_sort = self._expect(kind="IDENT").value
        self._expect(kind="IDENT", value="where")
        predicate = self._parse_expr()
        if name == "count":
            self._expect(kind="RPAREN")
            return {
                "kind": "count",
                "binder": {"name": binder_name, "sort": binder_sort},
                "predicate": predicate,
            }
        self._expect(kind="COMMA")
        value_expr = self._parse_expr()
        self._expect(kind="RPAREN")
        return {
            "kind": "call",
            "callee": "sum",
            "args": [
                {
                    "kind": "set_comp",
                    "binder": {"name": binder_name, "sort": binder_sort},
                    "predicate": predicate,
                },
                value_expr,
            ],
        }
