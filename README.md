# Tic-Tac-Toe Game

A terminal-based two-player Tic-Tac-Toe game implementation in Python, built according to the specification in SPEC.md.

## Features

- **Interactive two-player gameplay** - Players alternate between X and O
- **Automatic win detection** - Detects wins in rows, columns, and diagonals
- **Draw detection** - Identifies when the board is full with no winner
- **Input validation** - Validates player moves with clear error messages
- **Play again option** - Players can restart the game after it ends
- **Quit command** - Players can exit at any time with 'q'
- **Clear prompts** - User-friendly interface showing whose turn it is

## Requirements

- Python 3.6 or higher
- pytest (for running tests)

## Installation

1. Install pytest (required for testing):
```bash
pip install pytest
```

## How to Run the Game

Run the game with:
```bash
python tictactoe.py
```

### Gameplay Instructions

1. The game starts with an empty 3x3 board with numbered positions (1-9)
2. Player X always goes first
3. On each turn, enter a position number (1-9) to place your mark
4. The board positions are numbered as follows:
   ```
   1 | 2 | 3
   --+---+--
   4 | 5 | 6
   --+---+--
   7 | 8 | 9
   ```
5. Invalid moves will prompt you to enter a valid position
6. Enter 'q' at any time to quit the game
7. When the game ends, you'll be prompted to play again

### Example Game Session

```
Welcome to Tic-Tac-Toe!
Players will alternate turns. Enter position 1-9 or 'q' to quit.

1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9

Player X's turn - Enter position (1-9) or 'q' to quit: 5

X | 2 | 3
--+---+--
4 | X | 6
--+---+--
7 | 8 | 9

Player O's turn - Enter position (1-9) or 'q' to quit: 1
```

## How to Run Tests

Run the complete test suite with:
```bash
pytest test_tictactoe.py -v
```

To run a specific test class:
```bash
pytest test_tictactoe.py::TestGameBoardDisplay -v
```

To run a specific test:
```bash
pytest test_tictactoe.py::TestGameBoardDisplay::test_empty_board_initialization -v
```

## Test Coverage

The test suite includes automated tests for all requirements in SPEC.md:

- **Game Board Display** - Tests empty board and board with moves
- **Move Input and Validation** - Tests valid moves, invalid square numbers, occupied squares, and non-numeric input
- **Player Turn Rotation** - Tests first move and turn alternation
- **Win Detection** - Tests horizontal, vertical, and diagonal wins
- **Draw Detection** - Tests draw detection when board is full
- **Play Again Functionality** - Tests board reset
- **Quit Command** - Tests quit input recognition
- **Clear User Prompts** - Tests current player display

## Project Structure

```
.
├── SPEC.md              # Original specification (read-only)
├── tictactoe.py         # Main game implementation
├── test_tictactoe.py    # Automated test suite
└── README.md            # This file
```

## Implementation Details

### TicTacToeGame Class

The core game logic is implemented in the `TicTacToeGame` class with the following methods:

- `display_board()` - Displays the current board state
- `is_valid_move(position)` - Validates a move
- `make_move(position)` - Places a player's mark on the board
- `check_winner()` - Checks if the current player has won
- `is_board_full()` - Checks if the board is full
- `get_next_player()` - Switches to the next player
- `reset_board()` - Resets the board for a new game

### Main Game Loop

The `play_game()` function implements the main game loop, handling:

1. Board display
2. Player input with validation
3. Move execution
4. Win detection
5. Draw detection
6. Play again prompts
7. Quit handling

## Notes

- All position numbers are 1-indexed (1-9)
- The board is displayed in a fixed-width format for clarity
- Player X always goes first
- The game handles invalid input gracefully with clear error messages
- Tests verify compliance with all SPEC.md requirements
