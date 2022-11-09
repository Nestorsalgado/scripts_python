# # a las son inmutable y se utilizan (parentesis )

# frutas=("naranja","platano","guayaba")
# #podemos saber el largo de una tupla
# print(len(frutas))
# #acceder a un elemto con indices
# print(frutas[2])
# # navegacion inversa 
# print(frutas[-2])
# # acceder a un rango de valores 
# print(frutas[:2])


# #recorerr elementos
# for fruta in frutas:
#     print(fruta, end=" ")

# # conversion de tupla a lista 
# # se inmuta indirectamente la tupal
# frutaslis=list(frutas)
# frutaslis[0]="pera"
# frutas=tuple(frutaslis)
# print("\n",frutas)
# # es inmutable pero pueden ser eliminados por completo 
# del frutas

#Ejercicio. Dada la siguiente tupla, crear una lista que solo incluya los numeros menores a 5
tupla=(13,1,8,3,2,5,8)
#definimos lista vacia 
lista=[]
for i in tupla:
    if i<5:
        lista.append(i)
#saliendo del for imprimimos la lista ya iterada         
print(lista)
