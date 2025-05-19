
#!/usr/bin/env python3
"""
Punto de entrada principal para el juego de 3 en raya.
"""

from src.game import Game


def main():
    """Función principal del programa."""
    try:
        print("=== JUEGO DE 3 EN RAYA ===")
        print()
        
        # Solicitar nombres de los jugadores
        player1_name = input("Ingresa el nombre del Jugador 1 (X): ").strip()
        if not player1_name:
            player1_name = "Jugador 1"
            
        player2_name = input("Ingresa el nombre del Jugador 2 (O): ").strip()
        if not player2_name:
            player2_name = "Jugador 2"
        
        # Crear y ejecutar el juego
        game = Game(player1_name, player2_name)
        
        while True:
            game.play()
            
            # Preguntar si quieren jugar otra vez
            play_again = input("\n¿Quieren jugar otra vez? (s/n): ").strip().lower()
            if play_again not in ['s', 'si', 'sí', 'y', 'yes']:
                break
            
            game.reset_game()
            print("\n" + "="*30)
            print("NUEVO JUEGO")
            print("="*30)
        
        print("\n¡Gracias por jugar!")
        
    except KeyboardInterrupt:
        print("\n\n¡Hasta luego!")
    except Exception as e:
        print(f"\nOcurrió un error inesperado: {e}")
        print("Por favor, reporta este error.")


if __name__ == "__main__":
    main()