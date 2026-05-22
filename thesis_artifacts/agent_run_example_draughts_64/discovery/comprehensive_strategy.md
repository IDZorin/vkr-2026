# Comprehensive Translation Strategy for rules_core

## Overall Approach
This is a formal game rules document. The IR should model:
1. **Static definitions** (board geometry, piece types, initial positions) as AssertDecl facts
2. **Movement rules** as DeonticDecl obligations (what players MUST do)
3. **Capture rules** as DeonticDecl obligations (must capture when possible)
4. **Prohibitions** as DeonticDecl prohibitions (cannot capture own pieces, etc.)
5. **Permissions** as DeonticDecl permissions (choice capture, adjustment, etc.)

## Sorts needed (source-grounded)

### Board-related
- `BoardSquare` — a dark (playable) square on the board. Source: "dark squares"
- `BoardRow` — horizontal row 1-8. Source: "horizontal rows"
- `BoardColumn` — vertical column a-h. Source: "columns"
- `Diagonal` — a diagonal line of dark squares. Source: "diagonals"
- `Board` — the game board. Source: "board"

### Piece-related
- `Piece` — a game piece. Source: "piece"
- `Man` — subtype of Piece. Source: "man"
- `King` — subtype of Piece. Source: "king"
- `PieceColor` — enum: White, Black. Source: "white or light colored men, and 12 black or dark colored men"

### Move-related
- `Move` — a single move action. Source: "move"
- `Capture` — a capture action. Source: "capture"
- `MultipleCapture` — a chain of captures. Source: "multiple capture"
- `MoveDirection` — enum: Forward, Backward. Source: "forwards and backwards"

### Player-related
- `Player` — a participant. Source: "player"
- `Hand` — enum: OneHand, TwoHands. Source: "only one hand"

### Position-related
- `BoardPosition` — a specific square identified by row and column. Source: "square"

## Key Relations
- `square_row(BoardSquare, BoardRow)` — which row a square is in
- `square_column(BoardSquare, BoardColumn)` — which column
- `square_is_dark(BoardSquare)` — dark = playable
- `square_diagonal(BoardSquare, Diagonal)` — which diagonal(s) a square belongs to
- `piece_color(Piece, PieceColor)` — color of a piece
- `piece_type(Piece, PieceType)` — man or king
- `piece_square(Piece, BoardSquare)` — current position
- `piece_owner(Piece, Player)` — which player owns the piece
- `move_piece(Move, Piece)` — which piece is moved
- `move_from(Move, BoardSquare)` — source square
- `move_to(Move, BoardSquare)` — destination square
- `move_player(Move, Player)` — who made the move
- `capture_victim(Capture, Piece)` — which piece is captured
- `capture_chain(MultipleCapture, Capture)` — captures in a chain
- `is_legal_move(Move)` — whether a move is legal
- `is_legal_capture(Capture)` — whether a capture is legal
- `game_turn(Player)` — whose turn it is
- `is_promoted(Piece)` — whether a man has become a king
- `move_is_complete(Move)` — whether the move has been released

## Facts (AssertDecl)
1. Board has 64 squares, alternately black and white
2. Game played on dark squares → 32 active squares
3. Dark squares form diagonals; longest diagonal = 8 squares
4. Board placement rule (long diagonal at left of each player)
5. 12 white men, 12 black men
6. Initial positions: white on rows 1-3, black on rows 6-8
7. A piece can be a man or a king (definitional)
8. Man and king have different movement/capture
9. First move by white
10. King definition: man reaching last row, crowned
11. King moves forwards and backwards on diagonal

## Obligations (DeonticDecl)
1. Board must be placed with long diagonal at left of each player
2. Each move must be done with only one hand
3. A man must move forward diagonally to empty square of next row
4. Touch-move: if you touch a playable piece, you must play it
5. Man must capture when meeting opponent piece with free square behind
6. King must capture when encountering opponent piece with empty square(s) behind
7. During multiple capture, must continue jumping
8. Must crown man reaching last row
9. Capture must be clearly indicated
10. Must use one hand for capture and removing pieces
11. Must lift captured pieces in ascending/descending order

## Prohibitions (DeonticDecl)
1. Cannot capture one's own pieces
2. Forbidden to jump over own pieces during multiple capture
3. Forbidden to pass over same opponent piece more than once
4. Incorrect to touch opponent's pieces when not your turn
5. Using two hands for capture is incorrect

## Permissions (DeonticDecl)
1. Choice capture when multiple directions available
2. May adjust pieces with announcement ("I adjust")
3. May pass over same empty square more than once in multiple capture
4. King may be denoted by inversion of man (per competition regulations)
5. Player may put piece on another free square before release
6. King may occupy any free square by choice after capture
