
import pytest
from unittest.mock import patch
from src.player import Player


class TestPlayer:
    """Pruebas unitarias para la clase Player."""
    
    def test_player_initialization_valid(self):
        """Prueba la inicialización válida de un jugador."""
        player = Player("Juan", "X")
        assert player.name == "Juan"
        assert player.symbol == "X"
    
    def test_player_initialization_invalid_symbol(self):
        """Prueba la inicialización con símbolo inválido."""
        with pytest.raises(ValueError, match="Símbolo inválido"):
            Player("Juan", "Z")
    
    def test_player_str_representation(self):
        """Prueba la representación en string del jugador."""
        player = Player("Ana", "O")
        assert str(player) == "Ana (O)"
    
    def test_player_equality_same(self):
        """Prueba la igualdad entre jugadores idénticos."""
        player1 = Player("Juan", "X")
        player2 = Player("Juan", "X")
        assert player1 == player2
    
    def test_player_equality_different_name(self):
        """Prueba la desigualdad con nombres diferentes."""
        player1 = Player("Juan", "X")
        player2 = Player("Ana", "X")
        assert player1 != player2
    
    def test_player_equality_different_symbol(self):
        """Prueba la desigualdad con símbolos diferentes."""
        player1 = Player("Juan", "X")
        player2 = Player("Juan", "O")
        assert player1 != player2
    
    def test_player_equality_different_type(self):
        """Prueba la desigualdad con tipos diferentes."""
        player = Player("Juan", "X")
        assert player != "Juan (X)"
        assert player != 123
    
    @patch('builtins.input', side_effect=['1', '2'])
    def test_get_move_valid_input(self, mock_input):
        """Prueba la entrada válida de movimiento."""
        player = Player("Juan", "X")
        with patch('builtins.print'):  # Silenciar print
            row, col = player.get_move()
            assert row == 1
            assert col == 2
    
    @patch('builtins.input', side_effect=['invalid', '1'])
    def test_get_move_invalid_input(self, mock_input):
        """Prueba la entrada inválida de movimiento."""
        player = Player("Juan", "X")
        with patch('builtins.print'):  # Silenciar print
            with pytest.raises(ValueError, match="números válidos"):
                player.get_move()
    
    def test_validate_symbol_x(self):
        """Prueba validación de símbolo X."""
        player = Player("Test", "X")
        player.validate_symbol()  # No debe lanzar excepción
    
    def test_validate_symbol_o(self):
        """Prueba validación de símbolo O."""
        player = Player("Test", "O")
        player.validate_symbol()  # No debe lanzar excepción
    
    def test_validate_symbol_invalid(self):
        """Prueba validación de símbolo inválido."""
        with pytest.raises(ValueError):
            Player("Test", "Z")
            