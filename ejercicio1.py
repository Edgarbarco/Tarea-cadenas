import sys
#Escribir un programa que pregunte el nombre del usuario en la consola
#y un numero entero e imprima por pantalla en lineas distintas el nombre 
#del usuario tantas veces como el numero introducido

nombre = input (" Introduccir tu nombre: ")
n = int(input("Introduce un numero entero: "))
print((nombre + "\n") * int(n))