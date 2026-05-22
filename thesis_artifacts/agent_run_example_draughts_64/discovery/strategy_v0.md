# Strategy v0 — rules_core

## 1. User hints (verbatim)
(no hints set)

## 2. Entities and their methodology role

- **Player** (prelude type) — source phrase: "player" — role: agent who performs moves. Used as the agent in move execution obligations. No new sort needed; uses existing prelude/local entity.

- **Hand** (new sort, enum) — source phrase: "one hand" — role: instrument used to execute a move. Defined as an enum sort with exactly two members: `OneHand` and `TwoHands`. Grounded by source phrase "only one hand".

- **Move** (new sort) — source phrase: "move" — role: target of the execution action. Represents the abstract action of moving a piece. Not an event carrier; the carrier is `MoveExecution`.

- **MoveExecution** (new sort, event_class) — source phrase: "move must be done" — role: carrier sort that reifies the class of move-execution events. Attaches agent, instrument, and move via arity-2 relations. Rationale: avoids high-arity relation compression.

## 3. Relationships

The event carrier is `MoveExecution`. The following relations are declared:

- `move_execution_agent(MoveExecution, Player)` — ties the player as agent.
- `move_execution_hand(MoveExecution, Hand)` — ties the hand as instrument.
- `move_execution_move(MoveExecution, Move)` — ties the move as target.

No additional relations beyond those traceable to role_frame participants.

### Role Ownership Map

- source role: "player"
  owner/carrier: MoveExecution
  relation: move_execution_agent(MoveExecution, Player)
  status: formula

- source role: "one hand"
  owner/carrier: MoveExecution
  relation: move_execution_hand(MoveExecution, Hand)
  status: formula

- source role: "move"
  owner/carrier: MoveExecution
  relation: move_execution_move(MoveExecution, Move)
  status: formula

## 4. Per-clause translation strategy

- **c10**: "Each move must be done with only one hand."
  - Family: DeonticDecl_obligation
  - Modal handling: preserve_as_first_class (matches role_frame.modality.absorption_decision)
  - A4V3 sketch:
    ```
    obligation move_one_hand_obligation(move: Move, hand: Hand)
      action: execute
      target: move
      scope: MoveExecution
    ```
    Note: The obligation applies to the class of move executions; the singleton `MoveExecution` entity wires the class structure.

- **c4**: "The board has to be placed between the two players in such a way that the long diagonal starts at the left hand side of each player."
  - Family: DeonticDecl_obligation
  - Modal handling: preserve_as_obligation
  - A4V3 sketch:
    ```
    obligation board_placement_obligation(board: Board, player: Player)
      action: place
      target: board
      scope: BoardPlacement
    ```
    Note: `BoardPlacement` is a new carrier sort (event_class) for board placement obligations. `Board` is a new sort for the board entity.

- **c1, c2, c3, c5, c6, c7, c8, c9**: Descriptive/definitional facts.
  - Family: AssertDecl_fact
  - Modal handling: no_modal_present (c7's "can" absorbed as fact per classification)
  - A4V3 sketch (representative for c1):
    ```
    fact board_composition :
      board_has_squares(Board, 64) and board_has_colors(Board, AlternatingBlackWhite)
    ```

## 5. Critic feedback
(no critic feedback yet — v0 is initial strategy; subsequent versions populate this from VERIFY rounds)

## 6. Open questions and uncertainty
- The `BoardPlacement` carrier sort for c4 is not explicitly in role_frame's proposed_new_sorts; it may need to be added or the obligation attached to a different carrier. Awaiting precedent or drafter guidance.
- The `Board` sort is not in role_frame's proposed_new_sorts; it may be needed for c4 and c1-c3. Consider adding if multiple clauses reference it.
- The `Hand` enum members (`OneHand`, `TwoHands`) need explicit grounding — confirm source phrase "only one hand" is sufficient for `OneHand`; `TwoHands` may be unused but required for enum completeness.
