export class Board {
  constructor() {
    this.cells = Array(3).fill(null).map(() => Array(3).fill(0));
  }
  placePiece(row, col, player) {
    if (row < 0 || row > 2 || col < 0 || col > 2) {
      throw new Error(`Posición inválida: (${row}, ${col})`);
    }
    if (![1,2].includes(player)) {
      throw new Error(`Jugador inválido: ${player}`);
    }
    if (this.cells[row][col] !== 0) {
      throw new Error(`Celda ocupada: (${row}, ${col})`);
    }
    this.cells[row][col] = player;
  }
  getCell(row, col) {
    if (row < 0 || row > 2 || col < 0 || col > 2) {
      throw new Error(`Posición inválida: (${row}, ${col})`);
    }
    return this.cells[row][col];
  }
  reset() {
    this.cells = Array(3).fill(null).map(() => Array(3).fill(0));
  }
}