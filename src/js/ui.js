export class UI {
  constructor(boardEl, board, game) {
    this.boardEl = boardEl;
    this.board = board;
    this.game = game;
  }
  init() {
    this.boardEl.querySelectorAll('.cell').forEach(cell => {
      cell.addEventListener('click', () => this.handleClick(cell));
    });
  }
  handleClick(cell) {
    const row = +cell.dataset.row;
    const col = +cell.dataset.col;
    try {
      this.board.placePiece(row, col, this.game.getCurrentPlayer());
      const player = this.game.getCurrentPlayer();
      cell.textContent = player === 1 ? 'X' : 'O';
      cell.classList.add(`player${player}`);
      if (this.game.isWinner(player)) {
        setTimeout(() => alert(`¡Jugador ${player} ha ganado!`), 10);
        return;
      }
      this.game.nextTurn();
    } catch (e) {
      console.warn(e.message);
    }
  }
}