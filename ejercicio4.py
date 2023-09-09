#Los telefonos de una empresa tienen el siguiente formato prefijo-numero-extension
#donde el prefijo es el codigo del pais +34, y la extension tiene dos digitos 
#(por ejemplo +34-913724710-56). Escribir un programa que pregunte por un numero 
#de telefono con este formato y muestre por pantalla el numero de telefono sin el 
#prefijo y la extension.

tel = input("Introdude el numero de telefono con el formato +xx-xxxxxxxxx-xx: ")
print('El numero de telefono es ', tel[4:-3])