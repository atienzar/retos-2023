"""/*
 * Crea una función que reciba dos cadenas de texto casi iguales,
 * a excepción de uno o varios caracteres. 
 * La función debe encontrarlos y retornarlos en formato lista/array.
 * - Ambas cadenas de texto deben ser iguales en longitud.
 * - Las cadenas de texto son iguales elemento a elemento.
 * - No se pueden utilizar operaciones propias del lenguaje
 *   que lo resuelvan directamente.
 * 
 * Ejemplos:
 * - Me llamo mouredev / Me llemo mouredov -> ["e", "o"]
 * - Me llamo.Brais Moure / Me llamo brais moure -> [" ", "b", "m"]
 */ """


def compare_cads(cad1:str, cad2:str) -> list:
    wrong_chars=[]

    for index, char in enumerate(cad1):
      if char != cad2[index]:
        wrong_chars.append(cad2[index])
    
    return wrong_chars
 

print(compare_cads("Me llamo mouredev", "Me llemo mouredov"))
print(compare_cads("Me llamo.Brais Moure", "Me llamo brais moure"))
print(compare_cads("Me llamo.Brais Moure", "Me llamo.Brais Moure"))
print(compare_cads("", ""))