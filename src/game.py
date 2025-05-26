from .board import Board
from .player import Player


class Game:
    """Clase principal que maneja la lógica del juego 3 en raya."""
    
    def __init__(self, player1_name="Jugador 1", player2_name="Jugador 2"):
        """
        Inicializa un nuevo juego.
        
        Args:
            player1_name (str): Nombre del primer jugador
            player2_name (str): Nombre del segundo jugador
        """
        self.board = Board()
        self.player1 = Player(player1_name, 'X')
        self.player2 = Player(player2_name, 'O')
        self.current_player = self.player1
        self.game_over = False
        self.winner = None
    
    def switch_player(self):
        """Cambia el turno al otro jugador."""
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1
    
    def play_turn(self):
        """
        Ejecuta un turno completo del juego.
        
        Returns:
            bool: True si el turno fue exitoso, False en caso contrario
        """
        try:
            row, col = self.current_player.get_move()
            
            if not self.board.make_move(row, col, self.current_player.symbol):
                print("¡Movimiento inválido! Esa casilla está ocupada o fuera de rango.")
                return False
            
            return True
        except ValueError as e:
            print(f"Error: {e}")
            return False
    
    def check_game_status(self):
        """Verifica el estado del juego (ganador o empate)."""
        self.winner = self.board.check_winner()
        if self.winner:
            self.game_over = True
            return f"¡{self.get_player_by_symbol(self.winner).name} gana!"
        
        if self.board.is_full():
            self.game_over = True
            return "¡Empate!"
        
        return None
    
    def get_player_by_symbol(self, symbol):
        """
        Obtiene el jugador correspondiente a un símbolo.
        
        Args:
            symbol (str): Símbolo del jugador
            
        Returns:
            Player: El jugador correspondiente al símbolo
        """
        return self.player1 if self.player1.symbol == symbol else self.player2
    
    def play(self):
        """Ejecuta el bucle principal del juego."""
        print("¡Bienvenido al juego de 3 en raya!")
        print(f"{self.player1.name} juega con 'X'")
        print(f"{self.player2.name} juega con 'O'")
        status = None
        while not self.game_over:
            self.board.display()
            if self.play_turn():
                status = self.check_game_status()
                if status:
                    self.board.display()
                    print(status)
                    self.game_over = True  # Asegura que game_over sea True incluso si check_game_status está mockeado
                    break
                self.switch_player()
        # Si el bucle termina por otra razón y status no es None, asegura game_over
        if status:
            self.game_over = True
    
    def reset_game(self):
        """Reinicia el juego a su estado inicial."""
        self.board.reset()
        self.current_player = self.player1
        self.game_over = False
        self.winner = None
    
    def get_game_state(self):
        """
        Obtiene el estado actual del juego.
        
        Returns:
            dict: Diccionario con información del estado del juego
        """
        return {
            'board': [row[:] for row in self.board.grid],
            'current_player': str(self.current_player),
            'game_over': self.game_over,
            'winner': self.winner
        }