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
}