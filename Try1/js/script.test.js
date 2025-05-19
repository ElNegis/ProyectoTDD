/**creacion de carpet. funcion 3*/
const { checkWinner } = require('./script');

describe('Tres en Raya - Requerimiento 3', () => {

  test('No hay ganador si no se cumple condición', () => {
    global.board = [
      'X', 'O', 'X',
      'O', '',  'X',
      'O', '',  'O'
    ];
    expect(checkWinner()).toBe(false);
  });

  test('Gana jugador con línea horizontal', () => {
    global.board = [
      'X', 'X', 'X',
      'O', '',  'O',
      '',  '',  ''
    ];
    expect(checkWinner()).toBe(true);
  });

  test('Gana jugador con línea vertical', () => {
    global.board = [
      'O', 'X', '',
      'O', 'X', '',
      'O', '',  ''
    ];
    expect(checkWinner()).toBe(true);
  });

  test('Gana jugador con línea diagonal', () => {
    global.board = [
      'X', 'O', '',
      '',  'X', 'O',
      '',  '',  'X'
    ];
    expect(checkWinner()).toBe(true);
  });

});
