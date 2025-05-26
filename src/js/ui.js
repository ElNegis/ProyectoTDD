export class UI {
  constructor(boardEl, board, game) {
    this.boardEl = boardEl;
    this.board = board;
    this.game = game;
    this.statusEl = document.getElementById('status');
    this.restartBtn = document.getElementById('restart');
    this.cells = Array.from(this.boardEl.querySelectorAll('.cell'));
    this.active = true;
    if (this.restartBtn) {
      this.restartBtn.addEventListener('click', () => this.resetGame());
    }
  }
  init() {
    this.cells.forEach(cell => {
      cell.addEventListener('click', () => this.handleClick(cell));
    });
    this.updateStatus();
    this.clearBoard();
  }
  handleClick(cell) {
    if (!this.active || cell.textContent) return;
    const row = +cell.dataset.row;
    const col = +cell.dataset.col;
    try {
      this.board.placePiece(row, col, this.game.getCurrentPlayer());
      const player = this.game.getCurrentPlayer();
      cell.textContent = player === 1 ? 'X' : 'O';
      cell.classList.add(`player${player}`);
      if (this.game.isWinner(player)) {
        this.active = false;
        this.statusEl.textContent = `¡Jugador ${player === 1 ? 'X' : 'O'} ha ganado!`;
        this.highlightWin(player);
        return;
      }
      if (this.isDraw()) {
        this.active = false;
        this.statusEl.textContent = '¡Empate!';
        return;
      }
      this.game.nextTurn();
      this.updateStatus();
    } catch (e) {
      this.statusEl.textContent = e.message;
    }
  }
  updateStatus() {
    if (!this.active) return;
    const player = this.game.getCurrentPlayer();
    this.statusEl.textContent = `Turno de: Jugador ${player === 1 ? 'X' : 'O'}`;
  }
  isDraw() {
    return this.board.cells.flat().every(cell => cell !== 0);
  }
  resetGame() {
    this.board.reset();
    this.active = true;
    this.cells.forEach(cell => {
      cell.textContent = '';
      cell.classList.remove('player1', 'player2', 'win');
    });
    this.game.currentPlayer = 1;
    this.updateStatus();
  }
  clearBoard() {
    this.cells.forEach(cell => {
      cell.textContent = '';
      cell.classList.remove('player1', 'player2', 'win');
    });
  }
  highlightWin(player) {
    // Busca la línea ganadora y resalta las celdas
    const b = this.board.cells;
    // filas
    for (let i = 0; i < 3; i++) {
      if (b[i][0] === player && b[i][1] === player && b[i][2] === player) {
        this.cells.filter(cell => +cell.dataset.row === i).forEach(cell => cell.classList.add('win'));
        return;
      }
    }
    // columnas
    for (let i = 0; i < 3; i++) {
      if (b[0][i] === player && b[1][i] === player && b[2][i] === player) {
        this.cells.filter(cell => +cell.dataset.col === i).forEach(cell => cell.classList.add('win'));
        return;
      }
    }
    // diagonal principal
    if (b[0][0] === player && b[1][1] === player && b[2][2] === player) {
      [0,1,2].forEach(i => {
        this.cells.find(cell => +cell.dataset.row === i && +cell.dataset.col === i).classList.add('win');
      });
      return;
    }
    // diagonal secundaria
    if (b[0][2] === player && b[1][1] === player && b[2][0] === player) {
      [0,1,2].forEach(i => {
        this.cells.find(cell => +cell.dataset.row === i && +cell.dataset.col === 2-i).classList.add('win');
      });
      return;
    }
  }
}