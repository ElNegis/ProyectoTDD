const game = document.getElementById("game");
const statusDiv = document.getElementById("status");

let currentPlayer = "X";
let board = Array(9).fill("");
let gameOver = false;

function createBoard() {
  game.innerHTML = "";
  board.forEach((cellValue, index) => {
    const cell = document.createElement("div");
    cell.classList.add("cell");
    cell.dataset.index = index;
    cell.setAttribute("tabindex", "0");
    cell.setAttribute("role", "gridcell");
    cell.setAttribute("aria-label", `Celda ${index + 1}`);
    if (cellValue) {
      cell.textContent = cellValue;
      cell.classList.add(cellValue.toLowerCase());
    }
    cell.addEventListener("click", handleClick);
    cell.addEventListener("keydown", handleKey);
    game.appendChild(cell);
  });
  updateStatus();
}

function handleClick(e) {
  const index = e.target.dataset.index;
  if (board[index] || gameOver) return;
  makeMove(index, e.target);
}

function handleKey(e) {
  if (e.key === "Enter" || e.key === " ") {
    const index = e.target.dataset.index;
    if (!board[index] && !gameOver) {
      makeMove(index, e.target);
    }
  }
}

function makeMove(index, cellElem) {
  board[index] = currentPlayer;
  cellElem.textContent = currentPlayer;
  cellElem.classList.add(currentPlayer.toLowerCase());
  cellElem.classList.add("pop");
  setTimeout(() => cellElem.classList.remove("pop"), 300);

  if (checkWinner()) {
    updateStatus(`¡Ganó ${currentPlayer}! 🎉`);
    gameOver = true;
    highlightWinner();
    return;
  }

  if (board.every(cell => cell)) {
    updateStatus("¡Empate!");
    gameOver = true;
    return;
  }

  currentPlayer = currentPlayer === "X" ? "O" : "X";
  updateStatus();
}

function updateStatus(msg) {
  statusDiv.textContent = msg || `Turno de ${currentPlayer}`;
}

function highlightWinner() {
  const winPatterns = [
    [0,1,2], [3,4,5], [6,7,8],
    [0,3,6], [1,4,7], [2,5,8],
    [0,4,8], [2,4,6]
  ];
  winPatterns.forEach(pattern => {
    const [a, b, c] = pattern;
    if (board[a] && board[a] === board[b] && board[a] === board[c]) {
      document.querySelectorAll('.cell')[a].classList.add('winner');
      document.querySelectorAll('.cell')[b].classList.add('winner');
      document.querySelectorAll('.cell')[c].classList.add('winner');
    }
  });
}

function resetGame() {
  board = Array(9).fill("");
  currentPlayer = "X";
  gameOver = false;
  createBoard();
}

createBoard();
