#Escribir un programa que pregunte al usuario la fecha de su 
#nacimiento en formato dd/mm/aaaa y muestra por pantalla, el
#dia, el mes y el año. Adaptar el programa anterior para que 
#tambien funcione cuando el dia o el mes se introduzan con un 
#solo caracter.

fecha = input ("Introduce la fecha de tu nacimiento en formato dd/mm/aaaa: ")
print('Dia', fecha[:2])
print('Mes', fecha[3:5])
print('Año', fecha[6:])