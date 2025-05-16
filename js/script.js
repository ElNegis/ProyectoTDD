const game = document.getElementById("game");
const statusDiv = document.getElementById("status");

let currentPlayer = "X";
let board = Array(9).fill("");
let gameOver = false;

function createBoard() {
  game.innerHTML = "";
  board.forEach((_, index) => {
    const cell = document.createElement("div");
    cell.classList.add("cell");
    cell.dataset.index = index;
    cell.addEventListener("click", handleClick);
    game.appendChild(cell);
  });
  statusDiv.textContent = "Turno de X";
}

function handleClick(e) {
  const index = e.target.dataset.index;
  if (board[index] || gameOver) return;

  board[index] = currentPlayer;
  e.target.textContent = currentPlayer;

  if (checkWinner()) {
    statusDiv.textContent = `¡Ganó ${currentPlayer}! 🎉`;
    gameOver = true;
    return;
  }

  if (board.every(cell => cell)) {
    statusDiv.textContent = "¡Empate!";
    gameOver = true;
    return;
  }

  currentPlayer = currentPlayer === "X" ? "O" : "X";
  statusDiv.textContent = `Turno de ${currentPlayer}`;
}

function checkWinner() {
  const winPatterns = [
    [0,1,2], [3,4,5], [6,7,8],
    [0,3,6], [1,4,7], [2,5,8],
    [0,4,8], [2,4,6]
  ];
  return winPatterns.some(([a, b, c]) => {
    return board[a] && board[a] === board[b] && board[a] === board[c];
  });
}

function resetGame() {
  board = Array(9).fill("");
  currentPlayer = "X";
  gameOver = false;
  createBoard();
}

createBoard();
