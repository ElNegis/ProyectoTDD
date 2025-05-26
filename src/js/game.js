export class Game {
  constructor(board) {
    this.board = board;
    this.currentPlayer = 1;
  }
  nextTurn() {
    this.currentPlayer = this.currentPlayer === 1 ? 2 : 1;
    return this.currentPlayer;
  }
  getCurrentPlayer() {
    return this.currentPlayer;
  }
  /**
   * Comprueba si el jugador dado ha ganado.
   * Conecta 3 en lÃ­nea horizontal, vertical o diagonal.
   * @param {1|2} player
   * @returns {boolean}
   */
  isWinner(player) {
    const b = this.board.cells;
    // filas y columnas
    for (let i = 0; i < 3; i++) {
      if (b[i][0] === player && b[i][1] === player && b[i][2] === player) return true;
      if (b[0][i] === player && b[1][i] === player && b[2][i] === player) return true;
    }
    // diagonales
    if (b[0][0] === player && b[1][1] === player && b[2][2] === player) return true;
    //if (b[0][2] === player && b[1][1] === player && b[2][0] === player) return true;
    return false;
  }
}