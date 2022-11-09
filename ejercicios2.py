# #multiplica dos números sin usar el simbolo de multiplicar
# import re
# from tkinter import Y


# a=4
# b=8
# resultado=0
# for x in range (a):
#     resultado += b
# print(resultado)

# # ingresa nombre y apellido e imprimelo al reves 
# nombre= "sofia"
# apellido= "salgado"

# concatenacion = nombre + " " + apellido

# print(concatenacion [:: -1])

# #funcion que encuentre el menor de la lista 

# lista=[1,2,5,55,-24,-13]
# menor= "init"

# for x in lista:
#     if menor == "init":
#         menor= x
#     else: 
#         menor = x if x < menor else menor

# print("El número menor es: ", menor )

# #escribe una función que devulva el volumen de una esfera por su radio 
# #  4/ 3 * 3.14 r **3

# def calculaVolumen(r):
#     return 4 /3 * 3.14 * r ** 3

# resultado = calculaVolumen(6)
# print (resultado)  

# # escriba una funcion que indique si el usuario es mayor de edad

# def esMayor(usuario):
#     return usuario.edad > 17

# class Usuario:
#     def __init__(self, edad):
#         self.edad = edad

# usuario = Usuario (15)
# usuario2 = Usuario(23)

# resultado1= esMayor(usuario)
# resultado2= esMayor(usuario2)

# print(resultado1, resultado2)

# #  funcion par o impar
# def esPar(n):
#     return n % 2 == 0

# resultado = esPar(10)
# print(resultado)
# # funcion que indique cuantas vocales tinen una palabra

# palabra= "todOssabemospython"
# vocales=0
# for x in palabra:
#     y=x.lower()
#     vocales += 1 if y == "a" or y == "e" or y == "i" or y == "o" or y == "u" else 0  
# print(vocales)

# # ESCRIBE UNA APLICACIÓN QUE RECIBA UNA CANTIDAD INFINITA 
# # DE NUMEROS HASTA DECIR BASTA Y DEVUELVA LA SUMA DE LOS NUMEROS INGRESADOS 

# lista=[]

# print("Ingrese numeros hasta decir basta :")
# while True:
#     valor = input("Ingrese Valor:")
#     if valor == "basta":
#         break
#     else:
#         try:
#             valor = int(valor)
#             lista.append(valor)
#         except:
#             print("Dato invalido")
#             exit()

# resultado=0

# for x in lista:
#     resultado += x

# print(resultado)

def agregaNombreAArchivo (nombre, apellido):
    c= open("nombrecompleto.txt","a")
    c.write(nombre + " "+ apellido + "\n")


agregaNombreAArchivo("nestor", "salgado")