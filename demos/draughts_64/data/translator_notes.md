# Translator Notes - draughts_64 rules_core

## Scope

This entry formalizes IDF Draughts-64 source sections 2-4: material, movement, capture, and Brazilian capture differences.

## Arity And Role Notes

- `board_placed_between(Board, Player, Player)` is intentionally ternary. Roles are `board`, `player_one`, and `player_two`; the source phrase is "the board has to be placed between the two players." A carrier object would add little value because the relation is a simple placement frame.
- `all_squares_between_empty(BoardSquare, BoardSquare, Diagonal)` is intentionally ternary. Roles are `from_square`, `to_square`, and `diagonal`; it models the king-distance condition "all squares between source and target are empty" while keeping the diagonal explicit.

## Modeling Choices

- Diagram 1 is treated as formal rule content, not presentation scaffolding. It supplies the concrete 8x8 coordinate geometry, the 32 playable dark squares, and diagonal adjacency.
- `BoardSquare` denotes playable dark squares. The full 64-square board is preserved through `total_square_count(Board) = 64`, `active_square_count(Board) = 32`, and `light_square_coordinate(Column, Row)` facts for the 32 non-playable light coordinates.
- Concrete squares such as `SquareE3` are reified as `BoardSquare` entities with explicit `square_row`, `square_column`, `square_is_dark`, `square_diagonal`, and `adjacent_diagonal_squares` facts. This allows queries like "can a man on e3 move to d4?" to be answered from the IR rather than from external board knowledge.
- `same_diagonal(BoardSquare, BoardSquare)` is a square-to-square carrier relation derived from shared `square_diagonal(square, diagonal)` membership. This avoids using the square-to-diagonal relation as if it were square-to-square.
- `forward_next_row(BoardRow, PieceColor)` is color-relative: white advances from rows 1 to 8, black advances from rows 8 to 1. This is required because a single `next_row` function cannot represent both players' forward directions.
- Diagram 2 is treated as formal initial-position content. The 12 white and 12 black starting men are represented as concrete `InitialWhiteMan*` and `InitialBlackMan*` entities with `initial_piece_square`; active row-4 and row-5 squares are represented as `initial_empty_square`.
- Initial setup is modeled with `initial_man` and `initial_piece_square`, not with all future `Piece` instances. This avoids over-constraining kings or promoted pieces as if they must remain on the starting rows.
- Brazilian rules 4.16.2 and 4.16.3 are obligations where the source uses "is obliged" / "becomes"; only the later next-move capture is modeled as permission through `brazilian_next_move_capture_if_still_possible`.
- `move_after` is a lightweight temporal adjacency relation for turn alternation. It is not a full temporal logic layer.
