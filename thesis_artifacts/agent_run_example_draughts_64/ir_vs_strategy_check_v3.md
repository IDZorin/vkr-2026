# IR vs Strategy v0 consistency check (run 3)

- Verdict: **minor_drift**
- Summary: The IR implements the core strategy (entities, relations, obligations for c4 and c10) correctly with singleton carriers and proper role wiring. It adds many additional sorts, relations, and deontic declarations to cover the full ruleset (c8, c9, prohibitions, permissions) which are not in the strategy but are necessary for completeness. Missing explicit facts for c1 board dimensions/colors and c8/c9 rules, but these are covered implicitly by other facts and obligations.

## Matches

- ✓ Player sort (prelude type) used as agent (section 2 → sort Player)
- ✓ Hand sort with enum subtypes OneHand and TwoHands (section 2 → sort Hand = OneHand | TwoHands)
- ✓ Move sort declared (section 2 → sort Move)
- ✓ MoveExecution sort declared as event_class (section 2 → sort MoveExecution)
- ✓ Relation move_execution_agent(MoveExecution, Player) (section 3 → rel move_execution_agent : MoveExecution, Player)
- ✓ Relation move_execution_hand(MoveExecution, Hand) (section 3 → rel move_execution_hand : MoveExecution, Hand)
- ✓ Relation move_execution_move(MoveExecution, Move) (section 3 → rel move_execution_move : MoveExecution, Move)
- ✓ Obligation for move_one_hand (c10) with scope MoveExecution (section 4 (c10) → obligation one_hand_per_move ... scope: MoveExecutionClass)
- ✓ Obligation for board_placement (c4) with scope BoardPlacement (section 4 (c4) → obligation board_placement ... scope: BoardPlacementClass)
- ✓ BoardPlacement sort declared as event_class (section 4 (c4) → sort BoardPlacement)
- ✓ Board sort declared (section 4 (c4) → sort Board)
- ✓ Singleton entity MoveExecutionClass : MoveExecution (section 4 (c10) → entity MoveExecutionClass : MoveExecution)
- ✓ Singleton entity BoardPlacementClass : BoardPlacement (section 4 (c4) → entity BoardPlacementClass : BoardPlacement)
- ✓ Fact board_composition (c1) - board features (section 4 (c1) → fact board_features ... board_has_bases ...)
- ✓ Fact dark_squares_are_active (c2) (section 4 (c2) → fact dark_squares_are_active)
- ✓ Fact diagonals_are_skewed (c3) (section 4 (c3) → fact diagonals_are_skewed)
- ✓ Fact twelve_white and twelve_black (c5) (section 4 (c5) → fact twelve_white ... fact twelve_black)
- ✓ Fact white_on_rows_1_to_3 and black_on_rows_6_to_8 (c6) (section 4 (c6) → fact white_on_rows_1_to_3 ... fact black_on_rows_6_to_8)
- ✓ Fact piece_is_man_or_king (c7) (section 4 (c7) → fact piece_is_man_or_king)

## Missing from IR

- [soft] **Relation move_execution_instrument(MoveExecution, Hand) as per parts inventory role_instrument_one_hand** (strategy section 3 (parts inventory))
    fix: Rename move_execution_hand to move_execution_instrument or add an alias relation
- [soft] **Explicit fact for board_has_squares(Board, 64) as per c1 sketch** (strategy section 4 (c1))
    fix: Add fact: board_has_squares(Board, 64)
- [soft] **Explicit fact for board_has_colors(Board, AlternatingBlackWhite) as per c1 sketch** (strategy section 4 (c1))
    fix: Add fact: board_has_colors(Board, AlternatingBlackWhite)
- [strong] **Claim c8 (movement rules) not represented as fact** (strategy section 4 (c8))
    fix: Add fact for man moves forward diagonally one square
- [strong] **Claim c9 (capture rules) not represented as fact** (strategy section 4 (c9))
    fix: Add fact for mandatory capture and multiple capture rules

## Extra in IR (not in strategy)

- [soft] Multiple obligation declarations beyond c4 and c10 (e.g., man_move_forward, crown_promoted_man, touch_move, man_capture, king_capture, etc.) (IR obligation blocks after board_placement)
    rationale: These implement c8/c9 which are missing from strategy but are necessary for completeness; may be acceptable if they align with claims ledger
- [soft] Multiple prohibition declarations (self_capture, jump_own_piece, etc.) (IR prohibition blocks)
    rationale: Not mentioned in strategy but may be derived from claims ledger; acceptable if consistent
- [soft] Multiple permission declarations (choice_capture, repeat_empty_square, etc.) (IR permission blocks)
    rationale: Not mentioned in strategy but may be derived from claims ledger; acceptable if consistent
- [soft] Many additional sorts (BoardSquare, BoardRow, BoardColumn, Diagonal, Piece, Man, King, PieceColor, Capture, MultipleCapture, MoveDirection, String, Integer) (IR sort declarations)
    rationale: Necessary for implementing the rules; not explicitly in strategy but required for completeness
- [soft] Many additional relations (square_row, square_column, piece_color, piece_square, etc.) (IR rel declarations)
    rationale: Necessary for implementing the rules; not explicitly in strategy but required for completeness
- [soft] Fact move_execution_class_wiring with existential quantifier (IR fact move_execution_class_wiring)
    rationale: Wires the singleton entity; acceptable pattern
- [soft] Fact board_placement_class_wiring with existential quantifier (IR fact board_placement_class_wiring)
    rationale: Wires the singleton entity; acceptable pattern