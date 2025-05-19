import pytest
from src.board import Board


class TestBoard:
    """Pruebas unitarias para la clase Board."""
    
    def test_board_initialization(self):
        """Prueba la inicialización del tablero."""
        board = Board()
        assert board.size == 3
        assert len(board.grid) == 3
        assert all(len(row) == 3 for row in board.grid)
        assert all(cell == ' ' for row in board.grid for cell in row)
    
    def test_valid_move(self):
        """Prueba movimientos válidos."""
        board = Board()
        assert board.is_valid_move(0, 0) is True
        assert board.is_valid_move(1, 1) is True
        assert board.is_valid_move(2, 2) is True
    
    def test_invalid_move_out_of_bounds(self):
        """Prueba movimientos fuera de los límites."""
        board = Board()
        assert board.is_valid_move(-1, 0) is False
        assert board.is_valid_move(0, -1) is False
        assert board.is_valid_move(3, 0) is False
        assert board.is_valid_move(0, 3) is False
    
    def test_invalid_move_occupied_cell(self):
        """Prueba movimientos en celdas ocupadas."""
        board = Board()
        board.make_move(1, 1, 'X')
        assert board.is_valid_move(1, 1) is False
    
    def test_make_move_success(self):
        """Prueba la ejecución exitosa de un movimiento."""
        board = Board()
        assert board.make_move(0, 0, 'X') is True
        assert board.grid[0][0] == 'X'
    
    def test_make_move_failure(self):
        """Prueba el fallo al hacer un movimiento inválido."""
        board = Board()
        board.make_move(0, 0, 'X')
        assert board.make_move(0, 0, 'O') is False
        assert board.grid[0][0] == 'X'
    
    def test_check_winner_row(self):
        """Prueba la detección de ganador en fila."""
        board = Board()
        board.grid[0] = ['X', 'X', 'X']
        assert board.check_winner() == 'X'
    
    def test_check_winner_column(self):
        """Prueba la detección de ganador en columna."""
        board = Board()
        for i in range(3):
            board.grid[i][0] = 'O'
        assert board.check_winner() == 'O'
    
    def test_check_winner_diagonal_main(self):
        """Prueba la detección de ganador en diagonal principal."""
        board = Board()
        for i in range(3):
            board.grid[i][i] = 'X'
        assert board.check_winner() == 'X'
    
    def test_check_winner_diagonal_anti(self):
        """Prueba la detección de ganador en diagonal anti-principal."""
        board = Board()
        board.grid[0][2] = 'O'
        board.grid[1][1] = 'O'
        board.grid[2][0] = 'O'
        assert board.check_winner() == 'O'
    
    def test_no_winner(self):
        """Prueba cuando no hay ganador."""
        board = Board()
        assert board.check_winner() is None
        
        # Tablero parcialmente lleno sin ganador
        board.grid[0][0] = 'X'
        board.grid[0][1] = 'O'
        assert board.check_winner() is None
    
    def test_is_full_empty_board(self):
        """Prueba tablero vacío no está lleno."""
        board = Board()
        assert board.is_full() is False
    
    def test_is_full_partial_board(self):
        """Prueba tablero parcialmente lleno no está lleno."""
        board = Board()
        board.grid[0][0] = 'X'
        assert board.is_full() is False
    
    def test_is_full_complete_board(self):
        """Prueba tablero completamente lleno."""
        board = Board()
        for i in range(3):
            for j in range(3):
                board.grid[i][j] = 'X' if (i + j) % 2 == 0 else 'O'
        assert board.is_full() is True
    
    def test_reset_board(self):
        """Prueba el reinicio del tablero."""
        board = Board()
        board.grid[1][1] = 'X'
        board.reset()
        assert all(cell == ' ' for row in board.grid for cell in row)
    
    def test_get_cell_valid(self):
        """Prueba obtener celda válida."""
        board = Board()
        board.grid[1][1] = 'X'
        assert board.get_cell(1, 1) == 'X'
        assert board.get_cell(0, 0) == ' '
    
    def test_get_cell_invalid(self):
        """Prueba obtener celda inválida."""
        board = Board()
        assert board.get_cell(-1, 0) is None
        assert board.get_cell(0, -1) is None
        assert board.get_cell(3, 0) is None
        assert board.get_cell(0, 3) is None