export class Game {
  constructor(board) {
    this.board = board;
    this.currentPlayer = 1;
  }
  getCurrentPlayer() {
    return this.currentPlayer;
  }
}