import { Board } from '../src/js/board.js';

describe('Board', () => {
  let board;
  beforeEach(() => board = new Board());

  test('coloca pieza correctamente', () => {
    board.placePiece(0,0,1);
    expect(board.getCell(0,0)).toBe(1);
  });

  test('lanza error si celda ocupada', () => {
    board.placePiece(0,0,1);
    expect(() => board.placePiece(0,0,2)).toThrow();
  });
});