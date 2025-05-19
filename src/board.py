class Board:
    """Clase que representa el tablero del juego 3 en raya."""
    
    def __init__(self):
        """Inicializa un tablero vacío 3x3."""
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
        self.size = 3
    
    def display(self):
        """Muestra el tablero en la consola."""
        print("\n   0   1   2")
        print("  -----------")
        for i in range(self.size):
            print(f"{i} | {self.grid[i][0]} | {self.grid[i][1]} | {self.grid[i][2]} |")
            print("  -----------")
    
    def is_valid_move(self, row, col):
        """
        Verifica si un movimiento es válido.
        
        Args:
            row (int): Fila del movimiento
            col (int): Columna del movimiento
            
        Returns:
            bool: True si el movimiento es válido, False en caso contrario
        """
        if not (0 <= row < self.size and 0 <= col < self.size):
            return False
        return self.grid[row][col] == ' '
    
    def make_move(self, row, col, symbol):
        """
        Realiza un movimiento en el tablero.
        
        Args:
            row (int): Fila del movimiento
            col (int): Columna del movimiento
            symbol (str): Símbolo del jugador ('X' o 'O')
            
        Returns:
            bool: True si el movimiento fue exitoso, False en caso contrario
        """
        if self.is_valid_move(row, col):
            self.grid[row][col] = symbol
            return True
        return False
    
    def check_winner(self):
        """
        Verifica si hay un ganador en el tablero.
        
        Returns:
            str or None: El símbolo del ganador ('X' o 'O') o None si no hay ganador
        """
        # Verificar filas
        for row in self.grid:
            if row[0] == row[1] == row[2] != ' ':
                return row[0]
        
        # Verificar columnas
        for col in range(self.size):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] != ' ':
                return self.grid[0][col]
        
        # Verificar diagonales
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != ' ':
            return self.grid[0][0]
        
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != ' ':
            return self.grid[0][2]
        
        return None
    
    def is_full(self):
        """
        Verifica si el tablero está lleno.
        
        Returns:
            bool: True si el tablero está lleno, False en caso contrario
        """
        for row in self.grid:
            if ' ' in row:
                return False
        return True
    
    def reset(self):
        """Reinicia el tablero a su estado inicial."""
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
    
    def get_cell(self, row, col):
        """
        Obtiene el contenido de una celda específica.
        
        Args:
            row (int): Fila de la celda
            col (int): Columna de la celda
            
        Returns:
            str: Contenido de la celda
        """
        if 0 <= row < self.size and 0 <= col < self.size:
            return self.grid[row][col]
        return None