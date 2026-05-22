## Event
- carrier_kind: other
- reify_as_sort: MoveExecution
- source_phrase: "move must be done"
- rationale: The source describes a class of actions (moves) with multiple roles: agent (player), instrument (hand), and constraints (one hand). Reifying as a carrier sort allows attaching these roles via arity-2 relations instead of compressing into a high-arity relation.

## Modality
- in_source: must
- family: DeonticDecl / kind: obligation
- absorption: preserve_as_first_class
- rationale: The source confers an obligation on the player ('Each move must be done with only one hand') — a normative duty, not a descriptive fact.

## Participants
- role='agent' :: source="player"
    methodology_ctx: unknown — not surfaced in precedents
    general_role: A participant in a game who performs moves.
    proposed_modeling: use prelude type Player
    justification: no new sort — uses existing prelude/local entity
- role='instrument' :: source="one hand"
    methodology_ctx: unknown — not surfaced in precedents
    general_role: A physical hand used to execute a move in a board game.
    proposed_modeling: sort Hand with enum subtypes [OneHand | TwoHands]
    justification: Each move must be done with only one hand
- role='target' :: source="move"
    methodology_ctx: unknown — not surfaced in precedents
    general_role: An action in a board game where a piece is moved.
    proposed_modeling: sort Move; rel move_execution_hand(MoveExecution, Hand); rel move_execution_agent(MoveExecution, Player); rel move_execution_move(MoveExecution, Move)
    justification: Each move must be done with only one hand

## Ontology budget
- new_sorts: ['MoveExecution', 'Hand', 'Move']
- new_entities: []
- expected_total_sorts: 3
- expected_total_entities: 0
- rejected_temptations:
    - 'sort MoveType with subtypes [ManMove | KingMove]': Source does not enumerate move types as a closed set; the distinction is covered by existing piece sorts.
    - 'sort GamePhase': No source phrase demands a game-phase abstraction; the rules describe static constraints, not phases.

## Drafter directives (MUST follow)
- Reify MoveExecution as a carrier sort with arity-2 relations: move_execution_hand(MoveExecution, Hand), move_execution_agent(MoveExecution, Player), move_execution_move(MoveExecution, Move).
- Do NOT compress agent + instrument + move into a single 4-arg relation.
- Use DeonticDecl obligation block with action: execute, target: move, scope: MoveExecution.
- Define Hand as an enum sort with exactly two members: OneHand and TwoHands, grounded by source phrase 'only one hand'.