import pytest
from unittest.mock import patch, MagicMock, call
from src.game import Game
from src.player import Player
from src.board import Board


class TestGame:
    """Pruebas unitarias para la clase Game."""
    
    def test_game_initialization_default(self):
        """Prueba la inicialización por defecto del juego."""
        game = Game()
        assert game.player1.name == "Jugador 1"
        assert game.player1.symbol == "X"
        assert game.player2.name == "Jugador 2"
        assert game.player2.symbol == "O"
        assert game.current_player == game.player1
        assert game.game_over is False
        assert game.winner is None
        assert isinstance(game.board, Board)
    
    def test_game_initialization_custom_names(self):
        """Prueba la inicialización con nombres personalizados."""
        game = Game("Alice", "Bob")
        assert game.player1.name == "Alice"
        assert game.player2.name == "Bob"
        assert game.player1.symbol == "X"
        assert game.player2.symbol == "O"
    
    def test_switch_player(self):
        """Prueba el cambio de jugador."""
        game = Game("Alice", "Bob")
        assert game.current_player == game.player1
        
        game.switch_player()
        assert game.current_player == game.player2
        
        game.switch_player()
        assert game.current_player == game.player1
    
    @patch('src.player.Player.get_move', return_value=(1, 1))
    @patch('builtins.print')
    def test_play_turn_success(self, mock_print, mock_get_move):
        """Prueba un turno exitoso."""
        game = Game("Alice", "Bob")
        result = game.play_turn()
        
        assert result is True
        assert game.board.grid[1][1] == 'X'
        mock_get_move.assert_called_once()
    
    @patch('src.player.Player.get_move', return_value=(0, 0))
    @patch('builtins.print')
    def test_play_turn_invalid_move_occupied(self, mock_print, mock_get_move):
        """Prueba un turno con movimiento en casilla ocupada."""
        game = Game("Alice", "Bob")
        game.board.grid[0][0] = 'X'  # Ocupar la casilla
        
        result = game.play_turn()
        assert result is False
        mock_print.assert_called_with("¡Movimiento inválido! Esa casilla está ocupada o fuera de rango.")
    
    @patch('src.player.Player.get_move', return_value=(5, 5))
    @patch('builtins.print')
    def test_play_turn_invalid_move_out_of_bounds(self, mock_print, mock_get_move):
        """Prueba un turno con movimiento fuera de los límites."""
        game = Game("Alice", "Bob")
        
        result = game.play_turn()
        assert result is False
        mock_print.assert_called_with("¡Movimiento inválido! Esa casilla está ocupada o fuera de rango.")
    
    @patch('src.player.Player.get_move', side_effect=ValueError("Entrada inválida"))
    @patch('builtins.print')
    def test_play_turn_input_error(self, mock_print, mock_get_move):
        """Prueba un turno con error de entrada del usuario."""
        game = Game("Alice", "Bob")
        
        result = game.play_turn()
        assert result is False
        mock_print.assert_called_with("Error: Entrada inválida")
    
    def test_check_game_status_no_winner_empty_board(self):
        """Prueba el estado del juego en tablero vacío."""
        game = Game()
        status = game.check_game_status()
        
        assert status is None
        assert game.game_over is False
        assert game.winner is None
    
    def test_check_game_status_no_winner_partial_board(self):
        """Prueba el estado del juego con tablero parcialmente lleno sin ganador."""
        game = Game("Alice", "Bob")
        game.board.grid[0][0] = 'X'
        game.board.grid[0][1] = 'O'
        game.board.grid[1][0] = 'X'
        
        status = game.check_game_status()
        assert status is None
        assert game.game_over is False
        assert game.winner is None
    
    def test_check_game_status_winner_x(self):
        """Prueba el estado del juego con ganador X."""
        game = Game("Alice", "Bob")
        # Simular victoria en fila para X
        game.board.grid[0] = ['X', 'X', 'X']
        
        status = game.check_game_status()
        assert "Alice gana" in status
        assert game.game_over is True
        assert game.winner == 'X'
    
    def test_check_game_status_winner_o(self):
        """Prueba el estado del juego con ganador O."""
        game = Game("Alice", "Bob")
        # Simular victoria en columna para O
        game.board.grid[0][0] = 'O'
        game.board.grid[1][0] = 'O'
        game.board.grid[2][0] = 'O'
        
        status = game.check_game_status()
        assert "Bob gana" in status
        assert game.game_over is True
        assert game.winner == 'O'
    
    def test_check_game_status_tie(self):
        """Prueba el estado del juego con empate."""
        game = Game("Alice", "Bob")
        # Simular empate
        game.board.grid = [
            ['X', 'O', 'X'],
            ['O', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        
        status = game.check_game_status()
        assert status == "¡Empate!"
        assert game.game_over is True
        assert game.winner is None
    
    def test_get_player_by_symbol_x(self):
        """Prueba obtener jugador por símbolo X."""
        game = Game("Alice", "Bob")
        player = game.get_player_by_symbol('X')
        assert player == game.player1
        assert player.name == "Alice"
    
    def test_get_player_by_symbol_o(self):
        """Prueba obtener jugador por símbolo O."""
        game = Game("Alice", "Bob")
        player = game.get_player_by_symbol('O')
        assert player == game.player2
        assert player.name == "Bob"
    
    def test_reset_game(self):
        """Prueba el reinicio completo del juego."""
        game = Game("Alice", "Bob")
        # Modificar estado del juego
        game.board.grid[1][1] = 'X'
        game.board.grid[0][0] = 'O'
        game.current_player = game.player2
        game.game_over = True
        game.winner = 'X'
        
        # Reiniciar
        game.reset_game()
        
        # Verificar reinicio
        assert all(cell == ' ' for row in game.board.grid for cell in row)
        assert game.current_player == game.player1
        assert game.game_over is False
        assert game.winner is None
    
    def test_get_game_state_initial(self):
        """Prueba obtener el estado inicial del juego."""
        game = Game("Alice", "Bob")
        state = game.get_game_state()
        
        assert len(state['board']) == 3
        assert all(len(row) == 3 for row in state['board'])
        assert all(cell == ' ' for row in state['board'] for cell in row)
        assert state['current_player'] == "Alice (X)"
        assert state['game_over'] is False
        assert state['winner'] is None
    
    def test_get_game_state_with_moves(self):
        """Prueba obtener el estado del juego con movimientos."""
        game = Game("Alice", "Bob")
        game.board.grid[0][0] = 'X'
        game.board.grid[1][1] = 'O'
        game.current_player = game.player1
        
        state = game.get_game_state()
        
        assert state['board'][0][0] == 'X'
        assert state['board'][1][1] == 'O'
        assert state['current_player'] == "Alice (X)"
        assert state['game_over'] is False
        assert state['winner'] is None
    
    @patch('builtins.print')
    @patch('src.board.Board.display')
    @patch('src.game.Game.play_turn', return_value=True)
    @patch('src.game.Game.check_game_status', side_effect=[None, None, "¡Alice gana!"])
    def test_play_game_complete_with_winner(self, mock_check, mock_play_turn, mock_display, mock_print):
        """Prueba juego completo con ganador."""
        game = Game("Alice", "Bob")
        game.play()
        
        # Verificar que el juego terminó
        assert game.game_over is True
        # Verificar que se llamaron los métodos necesarios
        assert mock_play_turn.call_count == 3
        assert mock_check.call_count == 3
        assert mock_display.call_count >= 2  # Al menos inicial y final
    
    @patch('builtins.print')
    @patch('src.board.Board.display')
    @patch('src.game.Game.play_turn', side_effect=[False, True, True])
    @patch('src.game.Game.check_game_status', side_effect=[None, "¡Empate!"])
    def test_play_game_with_failed_turns(self, mock_check, mock_play_turn, mock_display, mock_print):
        """Prueba juego con turnos fallidos."""
        game = Game("Alice", "Bob")
        game.play()
        
        # Verificar que el turno fallido no cambió al jugador actual
        assert mock_play_turn.call_count == 3
        assert game.game_over is True
    
    @patch('builtins.print')
    @patch('src.board.Board.display')
    def test_play_game_initialization_messages(self, mock_display, mock_print):
        """Prueba los mensajes de inicialización del juego."""
        game = Game("Alice", "Bob")
        
        # Mock para que el juego termine inmediatamente
        with patch.object(game, 'play_turn', return_value=True), \
             patch.object(game, 'check_game_status', return_value="¡Alice gana!"):
            game.play()
        
        # Verificar mensajes de inicialización
        expected_calls = [
            call("¡Bienvenido al juego de 3 en raya!"),
            call("Alice juega con 'X'"),
            call("Bob juega con 'O'"),
            call("¡Alice gana!")
        ]
        
        # Verificar que se llamaron los prints esperados
        for expected_call in expected_calls:
            assert expected_call in mock_print.call_args_list
    
    def test_game_flow_integration(self):
        """Prueba de integración del flujo completo del juego."""
        game = Game("Alice", "Bob")
        
        # Simular secuencia de movimientos que resulte en victoria
        moves = [
            (0, 0, 'X'),  # Alice
            (0, 1, 'O'),  # Bob  
            (1, 0, 'X'),  # Alice
            (0, 2, 'O'),  # Bob
            (2, 0, 'X')   # Alice gana (columna izquierda)
        ]
        
        for i, (row, col, symbol) in enumerate(moves):
            # Verificar turno correcto
            expected_player = game.player1 if symbol == 'X' else game.player2
            assert game.current_player == expected_player
            
            # Hacer movimiento
            success = game.board.make_move(row, col, symbol)
            assert success is True
            
            # Verificar estado del juego
            status = game.check_game_status()
            
            if i < len(moves) - 1:
                # No debería haber ganador aún
                assert status is None
                assert game.game_over is False
                game.switch_player()
            else:
                # Último movimiento - Alice gana
                assert status == "¡Alice gana!"
                assert game.game_over is True
                assert game.winner == 'X'
    
    def test_game_state_consistency(self):
        """Prueba la consistencia del estado del juego."""
        game = Game("Player1", "Player2")
        
        # Estado inicial
        assert game.current_player == game.player1
        assert not game.game_over
        assert game.winner is None
        
        # Después de cambiar jugador
        game.switch_player()
        assert game.current_player == game.player2
        
        # Después de hacer movimiento
        game.board.make_move(1, 1, 'O')
        assert game.board.grid[1][1] == 'O'
        
        # Estado del juego debe ser consistente
        state = game.get_game_state()
        assert state['board'][1][1] == 'O'
        assert state['current_player'] == "Player2 (O)"
    
    def test_multiple_game_resets(self):
        """Prueba múltiples reinicios del juego."""
        game = Game("Alice", "Bob")
        
        for _ in range(3):
            # Hacer algunos movimientos
            game.board.make_move(0, 0, 'X')
            game.board.make_move(1, 1, 'O')
            game.switch_player()
            game.game_over = True
            game.winner = 'X'
            
            # Reiniciar
            game.reset_game()
            
            # Verificar estado limpio
            assert all(cell == ' ' for row in game.board.grid for cell in row)
            assert game.current_player == game.player1
            assert not game.game_over
            assert game.winner is None