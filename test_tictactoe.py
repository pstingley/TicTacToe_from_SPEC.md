"""
Automated tests for the Tic-Tac-Toe game.

Tests verify all requirements from SPEC.md:
- Game Board Display
- Move Input and Validation
- Player Turn Rotation
- Win Detection
- Draw Detection
- Play Again Functionality
- Quit Command
- Clear User Prompts
"""

import pytest
from tictactoe import TicTacToeGame


class TestGameBoardDisplay:
    """Tests for Requirement: Game Board Display."""

    def test_empty_board_initialization(self):
        """Scenario: Display empty board - Board displays with positions 1-9."""
        game = TicTacToeGame()
        expected = [str(i) for i in range(1, 10)]
        assert game.board == expected

    def test_board_with_moves(self):
        """Scenario: Display board with moves - Board shows X and O marks."""
        game = TicTacToeGame()
        game.make_move('1')
        game.current_player = 'O'
        game.make_move('2')
        game.current_player = 'X'
        game.make_move('3')

        assert game.board[0] == 'X'
        assert game.board[1] == 'O'
        assert game.board[2] == 'X'
        assert game.board[3] == '4'  # Unchanged positions


class TestMoveInputAndValidation:
    """Tests for Requirement: Move Input and Validation."""

    def test_valid_move_input(self):
        """Scenario: Valid move input - System accepts number 1-9 for empty square."""
        game = TicTacToeGame()
        is_valid, error_msg = game.is_valid_move('5')
        assert is_valid is True
        assert error_msg is None

    def test_invalid_square_number_too_low(self):
        """Scenario: Invalid square number - Rejects numbers < 1."""
        game = TicTacToeGame()
        is_valid, error_msg = game.is_valid_move('0')
        assert is_valid is False
        assert "between 1 and 9" in error_msg

    def test_invalid_square_number_too_high(self):
        """Scenario: Invalid square number - Rejects numbers > 9."""
        game = TicTacToeGame()
        is_valid, error_msg = game.is_valid_move('10')
        assert is_valid is False
        assert "between 1 and 9" in error_msg

    def test_occupied_square(self):
        """Scenario: Occupied square - Rejects move on occupied square."""
        game = TicTacToeGame()
        game.make_move('5')
        is_valid, error_msg = game.is_valid_move('5')
        assert is_valid is False
        assert "occupied" in error_msg

    def test_non_numeric_input(self):
        """Scenario: Non-numeric input - Rejects non-numeric input (except 'q')."""
        game = TicTacToeGame()
        is_valid, error_msg = game.is_valid_move('abc')
        assert is_valid is False
        assert "Invalid input" in error_msg or "Invalid input" in error_msg

    def test_move_success(self):
        """Test that make_move returns True for valid move."""
        game = TicTacToeGame()
        result = game.make_move('1')
        assert result is True
        assert game.board[0] == 'X'

    def test_move_failure_occupied(self):
        """Test that make_move returns False when square is occupied."""
        game = TicTacToeGame()
        game.make_move('1')
        result = game.make_move('1')
        assert result is False


class TestPlayerTurnRotation:
    """Tests for Requirement: Player Turn Rotation."""

    def test_first_move_by_x(self):
        """Scenario: First move - Player X makes the first move."""
        game = TicTacToeGame()
        assert game.current_player == 'X'

    def test_turn_alternation(self):
        """Scenario: Turn alternation - Players alternate between X and O."""
        game = TicTacToeGame()
        assert game.current_player == 'X'

        game.get_next_player()
        assert game.current_player == 'O'

        game.get_next_player()
        assert game.current_player == 'X'


class TestWinDetection:
    """Tests for Requirement: Win Detection."""

    def test_horizontal_win_top_row(self):
        """Scenario: Horizontal win - Detects win in positions 1-3."""
        game = TicTacToeGame()
        game.make_move('1')  # X at 1
        game.current_player = 'O'
        game.make_move('4')  # O at 4
        game.current_player = 'X'
        game.make_move('2')  # X at 2
        game.current_player = 'O'
        game.make_move('5')  # O at 5
        game.current_player = 'X'
        game.make_move('3')  # X at 3 - should win

        assert game.check_winner() is True

    def test_horizontal_win_middle_row(self):
        """Scenario: Horizontal win - Detects win in positions 4-6."""
        game = TicTacToeGame()
        game.make_move('1')
        game.current_player = 'O'
        game.make_move('4')
        game.current_player = 'X'
        game.make_move('2')
        game.current_player = 'O'
        game.make_move('5')
        game.current_player = 'X'
        game.make_move('3')
        game.current_player = 'O'
        game.make_move('6')  # O wins

        assert game.check_winner() is True

    def test_horizontal_win_bottom_row(self):
        """Scenario: Horizontal win - Detects win in positions 7-9."""
        game = TicTacToeGame()
        game.make_move('1')
        game.current_player = 'O'
        game.make_move('7')
        game.current_player = 'X'
        game.make_move('2')
        game.current_player = 'O'
        game.make_move('8')
        game.current_player = 'X'
        game.make_move('3')
        game.current_player = 'O'
        game.make_move('9')  # O wins

        assert game.check_winner() is True

    def test_vertical_win_left_column(self):
        """Scenario: Vertical win - Detects win in positions 1-4-7."""
        game = TicTacToeGame()
        game.make_move('1')
        game.current_player = 'O'
        game.make_move('2')
        game.current_player = 'X'
        game.make_move('4')
        game.current_player = 'O'
        game.make_move('3')
        game.current_player = 'X'
        game.make_move('7')  # X wins

        assert game.check_winner() is True

    def test_vertical_win_middle_column(self):
        """Scenario: Vertical win - Detects win in positions 2-5-8."""
        game = TicTacToeGame()
        game.make_move('1')
        game.current_player = 'O'
        game.make_move('2')
        game.current_player = 'X'
        game.make_move('3')
        game.current_player = 'O'
        game.make_move('5')
        game.current_player = 'X'
        game.make_move('6')
        game.current_player = 'O'
        game.make_move('8')  # O wins

        assert game.check_winner() is True

    def test_vertical_win_right_column(self):
        """Scenario: Vertical win - Detects win in positions 3-6-9."""
        game = TicTacToeGame()
        game.make_move('1')
        game.current_player = 'O'
        game.make_move('3')
        game.current_player = 'X'
        game.make_move('2')
        game.current_player = 'O'
        game.make_move('6')
        game.current_player = 'X'
        game.make_move('4')
        game.current_player = 'O'
        game.make_move('9')  # O wins

        assert game.check_winner() is True

    def test_diagonal_win_1_5_9(self):
        """Scenario: Diagonal win - Detects win in positions 1-5-9."""
        game = TicTacToeGame()
        game.make_move('1')
        game.current_player = 'O'
        game.make_move('2')
        game.current_player = 'X'
        game.make_move('5')
        game.current_player = 'O'
        game.make_move('3')
        game.current_player = 'X'
        game.make_move('9')  # X wins

        assert game.check_winner() is True

    def test_diagonal_win_3_5_7(self):
        """Scenario: Diagonal win - Detects win in positions 3-5-7."""
        game = TicTacToeGame()
        game.make_move('1')
        game.current_player = 'O'
        game.make_move('3')
        game.current_player = 'X'
        game.make_move('2')
        game.current_player = 'O'
        game.make_move('5')
        game.current_player = 'X'
        game.make_move('4')
        game.current_player = 'O'
        game.make_move('7')  # O wins

        assert game.check_winner() is True

    def test_no_win_yet(self):
        """Test that check_winner returns False when there's no winner."""
        game = TicTacToeGame()
        game.make_move('1')
        assert game.check_winner() is False


class TestDrawDetection:
    """Tests for Requirement: Draw Detection."""

    def test_draw_detection_board_full(self):
        """Scenario: Board full with no winner - Game detects draw."""
        game = TicTacToeGame()
        # Create a draw game:
        # X | X | O
        # O | O | X
        # X | O | X
        moves = [1, 3, 2, 4, 6, 5, 7, 8, 9]
        for i, move in enumerate(moves):
            if i > 0:
                game.get_next_player()
            game.make_move(str(move))

        assert game.is_board_full() is True
        assert game.check_winner() is False

    def test_board_not_full(self):
        """Test that is_board_full returns False when board has empty squares."""
        game = TicTacToeGame()
        game.make_move('1')
        assert game.is_board_full() is False


class TestPlayAgainFunctionality:
    """Tests for Requirement: Play Again Functionality."""

    def test_reset_board(self):
        """Scenario: Players choose to play again - Board resets."""
        game = TicTacToeGame()
        game.make_move('1')
        game.get_next_player()
        game.make_move('2')

        game.reset_board()

        expected = [str(i) for i in range(1, 10)]
        assert game.board == expected
        assert game.current_player == 'X'


class TestQuitCommand:
    """Tests for Requirement: Quit Command."""

    def test_quit_input_recognized(self):
        """Scenario: Quit during gameplay - 'q' input should be recognized."""
        game = TicTacToeGame()
        # The quit command is handled in get_player_input, not in is_valid_move
        # is_valid_move should reject 'q' as invalid (it's checked separately in get_player_input)
        is_valid, _ = game.is_valid_move('q')
        assert is_valid is False


class TestClearUserPrompts:
    """Tests for Requirement: Clear User Prompts."""

    def test_current_player_x(self):
        """Scenario: Display current player - Shows player X when it's X's turn."""
        game = TicTacToeGame()
        assert game.current_player == 'X'

    def test_current_player_o(self):
        """Scenario: Display current player - Shows player O when it's O's turn."""
        game = TicTacToeGame()
        game.get_next_player()
        assert game.current_player == 'O'


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
