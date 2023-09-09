#Escribir un programa que pregunte por consola el precio de un
#producto en euros con dos decimales y muestre por pantalla el
#numero de euros y el numero de centimos del precio introducido.

precio = input("Introduce el precio del producto con dos decimales: ")
print(precio[:precio.find('.')], 'euros y', precio[precio.find('.')+1:], 'centimos.')
 