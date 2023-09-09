#Escribir un programa que pregunte el nombre completo del usuario en la consola
#y despues muestre por pantalla el nombre completo del usuario tres veces, una 
#con todas las letras minusculas, otra con todas las letras mayusculas y otra 
#solo con la primera letra del nombre y de los apellidos en mayuscula.
#El usuario puede introducir su nombre combinando mayusculas y minusculas como quiera.

nombre_completo = input("Introduce tu nombre completo: ")

nombre_min = nombre_completo.lower()
print("nombre en minusculas:")

nombre_may = nombre_completo.upper()
print("nombre en mayusculas:")

palabras = nombre_completo.split()

nombre_cap = ''.join([palabra.capitalize() for palabra in palabras])
print("Nombre con la primera letra en mayuscula:", nombre_cap)