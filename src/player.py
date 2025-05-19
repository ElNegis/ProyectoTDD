class Player:
    """Clase que representa un jugador del juego 3 en raya."""
    
    def __init__(self, name, symbol):
        """
        Inicializa un nuevo jugador.
        
        Args:
            name (str): Nombre del jugador
            symbol (str): Símbolo del jugador ('X' o 'O')
        """
        self.name = name
        self.symbol = symbol
        self.validate_symbol()
    
    def validate_symbol(self):
        """Valida que el símbolo sea válido ('X' o 'O')."""
        if self.symbol not in ['X', 'O']:
            raise ValueError(f"Símbolo inválido: {self.symbol}. Debe ser 'X' o 'O'")
    
    def get_move(self):
        """
        Solicita al jugador que ingrese su movimiento.
        
        Returns:
            tuple: Tupla (fila, columna) del movimiento elegido
            
        Raises:
            ValueError: Si la entrada no es válida
        """
        try:
            print(f"\nTurno de {self.name} ({self.symbol})")
            row = int(input("Ingresa la fila (0-2): "))
            col = int(input("Ingresa la columna (0-2): "))
            return row, col
        except ValueError:
            raise ValueError("Por favor, ingresa números válidos")
    
    def __str__(self):
        """Representación en string del jugador."""
        return f"{self.name} ({self.symbol})"
    
    def __eq__(self, other):
        """Compara dos jugadores por igualdad."""
        if not isinstance(other, Player):
            return False
        return self.name == other.name and self.symbol == other.symbol