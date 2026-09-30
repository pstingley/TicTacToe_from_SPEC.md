"""
Tic-Tac-Toe Game Implementation

A terminal-based two-player Tic-Tac-Toe game where players alternate turns
to place their marks (X or O) on a 3x3 board with automatic win and draw detection.
"""


class TicTacToeGame:
    """Represents a Tic-Tac-Toe game."""

    def __init__(self):
        """Initialize the game with an empty board."""
        self.board = [str(i) for i in range(1, 10)]
        self.current_player = 'X'

    def display_board(self):
        """Display the current game board in the specified format."""
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("--+---+--")
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("--+---+--")
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def is_valid_move(self, position):
        """
        Check if a move is valid.

        Args:
            position: The position (1-9) where the player wants to place their mark.

        Returns:
            tuple: (is_valid, error_message)
                is_valid (bool): True if the move is valid, False otherwise.
                error_message (str): An error message if invalid, None if valid.
        """
        # Check if position is numeric
        try:
            pos = int(position)
        except ValueError:
            return False, "Invalid input. Please enter a number between 1 and 9."

        # Check if position is in range 1-9
        if pos < 1 or pos > 9:
            return False, "Invalid square number. Please enter a number between 1 and 9."

        # Check if square is already occupied
        if self.board[pos - 1] in ('X', 'O'):
            return False, f"Square {pos} is already occupied. Please choose another square."

        return True, None

    def make_move(self, position):
        """
        Make a move by placing the current player's mark on the board.

        Args:
            position: The position (1-9) where the player wants to place their mark.

        Returns:
            bool: True if the move was successful, False otherwise.
        """
        pos = int(position)
        if self.board[pos - 1] in ('X', 'O'):
            return False
        self.board[pos - 1] = self.current_player
        return True

    def check_winner(self):
        """
        Check if the current player has won.

        Returns:
            bool: True if the current player has three in a row, False otherwise.
        """
        b = self.board
        # Check rows
        if b[0] == b[1] == b[2] == self.current_player:
            return True
        if b[3] == b[4] == b[5] == self.current_player:
            return True
        if b[6] == b[7] == b[8] == self.current_player:
            return True

        # Check columns
        if b[0] == b[3] == b[6] == self.current_player:
            return True
        if b[1] == b[4] == b[7] == self.current_player:
            return True
        if b[2] == b[5] == b[8] == self.current_player:
            return True

        # Check diagonals
        if b[0] == b[4] == b[8] == self.current_player:
            return True
        if b[2] == b[4] == b[6] == self.current_player:
            return True

        return False

    def is_board_full(self):
        """
        Check if the board is full.

        Returns:
            bool: True if all squares are occupied, False otherwise.
        """
        return all(cell in ('X', 'O') for cell in self.board)

    def get_next_player(self):
        """Switch to the next player."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_board(self):
        """Reset the board for a new game."""
        self.board = [str(i) for i in range(1, 10)]
        self.current_player = 'X'


def get_player_input(game):
    """
    Get input from the current player.

    Args:
        game: The TicTacToeGame instance.

    Returns:
        str: The player's input ('q' to quit, or a position number 1-9).
    """
    while True:
        prompt = f"Player {game.current_player}'s turn - Enter position (1-9) or 'q' to quit: "
        user_input = input(prompt).strip()

        # Check for quit command
        if user_input.lower() == 'q':
            return 'q'

        # Validate move
        is_valid, error_msg = game.is_valid_move(user_input)
        if not is_valid:
            print(error_msg)
            continue

        return user_input


def play_game():
    """Main game loop."""
    game = TicTacToeGame()

    print("Welcome to Tic-Tac-Toe!")
    print("Players will alternate turns. Enter position 1-9 or 'q' to quit.\n")

    while True:
        game.display_board()
        print()

        # Get player input
        player_input = get_player_input(game)

        # Check for quit
        if player_input == 'q':
            print("Thanks for playing! Goodbye.")
            break

        # Make the move
        game.make_move(player_input)

        # Check for win
        if game.check_winner():
            print()
            game.display_board()
            print()
            print(f"Player {game.current_player} wins! Congratulations!")
            print()

            # Ask to play again
            while True:
                play_again = input("Would you like to play again? (yes/no): ").strip().lower()
                if play_again in ('yes', 'y'):
                    game.reset_board()
                    print()
                    break
                elif play_again in ('no', 'n'):
                    print("Thanks for playing! Goodbye.")
                    return
                else:
                    print("Please enter 'yes' or 'no'.")

        # Check for draw
        elif game.is_board_full():
            print()
            game.display_board()
            print()
            print("It's a draw! The board is full.")
            print()

            # Ask to play again
            while True:
                play_again = input("Would you like to play again? (yes/no): ").strip().lower()
                if play_again in ('yes', 'y'):
                    game.reset_board()
                    print()
                    break
                elif play_again in ('no', 'n'):
                    print("Thanks for playing! Goodbye.")
                    return
                else:
                    print("Please enter 'yes' or 'no'.")

        else:
            # Continue to next turn
            game.get_next_player()
            print()


if __name__ == '__main__':
    play_game()
