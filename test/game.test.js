import { Game } from '../src/js/game.js';
import { Board } from '../src/js/board.js';

describe('Game', () => {
  let game;
  beforeEach(() => {
    game = new Game(new Board());
  });

  test('jugador inicial es 1', () => {
    expect(game.getCurrentPlayer()).toBe(1);
  });

  test('cambia turno correctamente', () => {
    game.nextTurn();
    expect(game.getCurrentPlayer()).toBe(2);
  });

  test('detecta victoria por fila', () => {
    const b = game.board;
    b.placePiece(1, 0, 1);
    b.placePiece(1, 1, 1);
    b.placePiece(1, 2, 1);
    expect(game.isWinner(1)).toBe(true);
  });

  test('detecta victoria por columna', () => {
    const b = game.board;
    b.placePiece(0, 2, 2);
    b.placePiece(1, 2, 2);
    b.placePiece(2, 2, 1);
    expect(game.isWinner(2)).toBe(true);
  });

  test('detecta victoria diagonal principal', () => {
    const b = game.board;
    b.placePiece(0, 0, 1);
    b.placePiece(1, 1, 1);
    b.placePiece(2, 2, 1);
    expect(game.isWinner(1)).toBe(true);
  });

  test('detecta victoria diagonal secundaria', () => {
    const b = game.board;
    b.placePiece(0, 2, 2);
    b.placePiece(1, 1, 2);
    b.placePiece(2, 0, 2);
    expect(game.isWinner(2)).toBe(true);
  });

  test('no marca victoria equivocada', () => {
    const b = game.board;
    b.placePiece(0, 0, 1);
    b.placePiece(0, 1, 2);
    b.placePiece(0, 2, 1);
    expect(game.isWinner(1)).toBe(false);
    expect(game.isWinner(2)).toBe(false);
  });
});