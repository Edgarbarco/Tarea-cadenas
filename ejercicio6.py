#Escribir un programa que pida al usuario que introduzcauna
#frase en la consola y una vocal, y despues muestre por
#pantalla la misma frase pero con la vocal introducida en
#mayuscula.

frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal en minuscula: ")
print(frase.replace(vocal, vocal.upper()))