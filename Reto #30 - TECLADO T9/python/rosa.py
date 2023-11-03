"""
/*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
 */
"""
import string

def t9_to_text(sequence:str)->str:

    text = ""
    t9=[' ', ',.?!', 'ABC', 'DEF', 'GHI','JKL','MNO', 'PQRS','TUV','WXYZ' ]
    
    # lo que importa es la longitud de cada char
    if not check_t9(sequence):
        text = "Error"
        return text
    
    for letter in sequence.split("-"):
        index= int(letter[0])
        # text += (t9[index])[len(letter)-1]
        text += (t9[index])[len(letter) % 3 -1]
    
    return text  


def check_t9(sequence:str) ->bool:

    if not sequence:
        return False

    for numbers in sequence.split("-"):
        first_char = numbers[0]
        for char in numbers:
            # if type(char) != int and  char != first_char:
            if not char.isdigit() or char != first_char:
                return False
    return True


print(t9_to_text("6-666-88-777-33-3-33-888"))
print(t9_to_text("6-666666-88-777-33-3-33-888"))
print(t9_to_text("6-676-88-777-33-3-33-888"))
print(t9_to_text("6-3aa-88-777-33-3-33-888"))
print(t9_to_text(""))
