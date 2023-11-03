"""
/*
 * Crea un programa capaz de gestionar una pieza de Tetris.
 * - La pantalla de juego tiene 10 filas y 10 columnas representadas por símbolos 🔲
 * - La pieza de tetris a manejar será la siguiente (si quieres, puedes elegir otra):
 *   🔳
 *   🔳🔳🔳
 * - La pieza aparecerá por primera vez en la parte superior izquierda de la pantalla de juego.
 *   🔳🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔳🔳🔳🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
 * - Debes desarrollar una función capaz de desplazar y rotar la pieza en el tablero,
 *   recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en la pantalla  de juego.
 * - Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
 * - Debes tener en cuenta los límites de la pantalla de juego.
 */
"""

MAX_COL = 10
MAX_ROW = 10

def rotar_90_grados(pieza: list) -> list:

    return pieza


def move_right(tetris: list):

    new_tetris=[]
    for row in tetris:
        new_row=''
        next_char="🔲"

        for i in range(MAX_ROW):
            if row[i] == "🔲" and next_char=="🔳":
                new_row += "🔳"
                next_char="🔲"
            elif row[i] == "🔳" and next_char=="🔳":
                new_row += "🔳"
                next_char="🔳"
            elif row[i] == "🔳" and next_char=="🔲":
                new_row += "🔲"
                next_char="🔳"
            elif row[i] == "🔲" and next_char=="🔲":
                new_row += "🔲"
                next_char=="🔲"
            else:
                raise Exception("Error con el tipo de fila!")

        new_tetris.append(new_row)
    return new_tetris
 


tetris = ["🔳🔲🔲🔲🔲🔲🔲🔲🔲🔲",
          "🔳🔳🔳🔲🔲🔲🔲🔲🔲🔲",
          "🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲",
          "🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲",
          "🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲",
          "🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲",
          "🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲",
          "🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲",
          "🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲",
          "🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲" ]

# for row in tetris:
#     print(row)

print('--------------->')

tetris = move_right(tetris)
for row in tetris:
    print(row)

