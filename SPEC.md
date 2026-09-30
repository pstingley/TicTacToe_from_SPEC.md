# game/tictactoe Specification

## Purpose
Provides a terminal-based two-player Tic-Tac-Toe game where players alternate turns to place their marks (X or O) on a 3x3 board, with automatic win and draw detection, and support for replaying games.

## Requirements

### Requirement: Game Board Display
The system SHALL display a 3x3 Tic-Tac-Toe board with nine numbered positions (1-9) in a fixed-width format with proper alignment and SHALL show the current state of each square with 'X', 'O', or the position number if empty. The board format SHALL be:
```
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9
```

#### Scenario: Display empty board
- **WHEN** the game starts
- **THEN** the board displays with positions 1-9 in the fixed-width format above, all empty

#### Scenario: Display board with moves
- **WHEN** players have made moves
- **THEN** the board shows X and O marks in their respective positions

### Requirement: Move Input and Validation
The system SHALL accept player input to select a square (1-9) and SHALL reject invalid moves with a clear error message.

#### Scenario: Valid move input
- **WHEN** a player enters a number from 1 to 9 for an empty square
- **THEN** the system accepts the move and places the player's mark on the board

#### Scenario: Invalid square number
- **WHEN** a player enters a number outside the range 1-9
- **THEN** the system displays an error message and prompts for input again

#### Scenario: Occupied square
- **WHEN** a player attempts to place a mark on an already occupied square
- **THEN** the system displays an error message indicating the square is taken and prompts for input again

#### Scenario: Non-numeric input
- **WHEN** a player enters non-numeric input (other than 'q')
- **THEN** the system displays an error message and prompts for input again

### Requirement: Player Turn Rotation
The system SHALL alternate turns between player X and player O, starting with player X.

#### Scenario: First move
- **WHEN** the game starts
- **THEN** player X is prompted to make the first move

#### Scenario: Turn alternation
- **WHEN** player X makes a move
- **THEN** player O is prompted for the next move, and turns continue to alternate

### Requirement: Win Detection
The system SHALL detect when a player has won by placing three of their marks in a row, column, or diagonal, and SHALL declare that player the winner.

#### Scenario: Horizontal win
- **WHEN** a player places their mark to complete three in a row (positions 1-3, 4-6, or 7-9)
- **THEN** the system displays the final board state and announces the player as the winner

#### Scenario: Vertical win
- **WHEN** a player places their mark to complete three in a column (positions 1-4-7, 2-5-8, or 3-6-9)
- **THEN** the system displays the final board state and announces the player as the winner

#### Scenario: Diagonal win
- **WHEN** a player places their mark to complete three in a diagonal (positions 1-5-9 or 3-5-7)
- **THEN** the system displays the final board state and announces the player as the winner

### Requirement: Draw Detection
The system SHALL detect when the board is full and no player has won, and SHALL announce the game as a draw.

#### Scenario: Board full with no winner
- **WHEN** all nine squares are filled with marks and no player has three in a row/column/diagonal
- **THEN** the system displays the final board state and announces that the game is a draw

### Requirement: Play Again Functionality
After a game ends, the system SHALL ask whether the players want to play again and SHALL reset the board if they choose to continue.

#### Scenario: Players choose to play again
- **WHEN** a game ends and players are asked if they want to play again
- **THEN** responding affirmatively resets the board and starts a new game with X going first

#### Scenario: Players choose not to play again
- **WHEN** a game ends and players choose not to play again
- **THEN** the system exits gracefully

### Requirement: Quit Command
The system SHALL allow a player to quit the game at any time by entering 'q', and the system SHALL exit immediately without playing again.

#### Scenario: Quit during gameplay
- **WHEN** a player enters 'q' instead of a move number
- **THEN** the system exits the game immediately without prompting to play again

### Requirement: Clear User Prompts
The system SHALL display clear prompts indicating which player's turn it is and requesting a valid input (1-9 or 'q').

#### Scenario: Display current player
- **WHEN** waiting for a player's move
- **THEN** the system displays a prompt showing whose turn it is (e.g., "Player X's turn")

#### Scenario: Display input instructions
- **WHEN** waiting for a player's move
- **THEN** the prompt includes instructions for valid input (enter 1-9 or 'q' to quit)
