"""
/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */
"""
import string

def calculate_col(cad: str) -> int :
    number = 0
    letters = { 'A': 1, 'B' : 2, 'C':3, 'D': 4, 'E':5, 'F':6,'G':7, 'H':8, 'I':9, 'J': 10, 'K':11,
               'L':12,'M':13, 'N':14,'O':15, 'P':16, 'Q':17, 'R':18 , 'S':19, 'T':20, 'U':21, 'V':22,
               'W':23, 'X':24, 'Y': 25, 'Z':26}
    
    #letters = string.ascii_uppercase()

    posicion = len(cad) -1
    for character in cad:
        number  = number * 26 + letters[character.upper()]
        posicion -= 1

    print(f'El numero es: {number}')
    return number

print(calculate_col('A'))
print(calculate_col('Z'))
print(calculate_col('AA'))
print(calculate_col('CA'))
print(calculate_col('BCA'))
print(calculate_col('AAA'))