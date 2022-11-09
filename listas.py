nombres=["juan","karla","ricardo","maria"]
# # # accedemos a los elementos por su indice 
# # print(nombres[1])

# # #accedemos a los elementos de manera inversa 
# # print(nombres[-1])
# # print(nombres[-2])
# # # acceder a un rango sin incluir el indice 2
# # print(nombres[0:2])
# # #ir del inicio de la lista al indice (sin inclirlo)
# # print(nombres[:3])
# # #desde el indice indicado hasta el final
# # print(nombres[1:])
# # #cambiar valor del indice 
# # nombres[3]="ivone"
# # print(nombres)
# # #iterar ubna lista 

# # for a in nombres:
# #     print(a)
# # else:
# #     print("esos fueron todos los nombres de la lista ")

# # # longuitud de lista 
# # print(len(nombres))
# # #agrgar un elemento a la lista 
# # nombres.append("lorenzo")
# # #incertar elemento en indice especifico (posicion, elemento) los demas se recorren a la derecha 
# # nombres.insert(1,"octavio")
# # print(nombres)
# # #remover elemento por valor
# # nombres.remove("octavio")
# # #remover ultimo valor agregado (pilas)
# # nombres.pop()
# # print(nombres)
# # #remover un indice indicado
# # del nombres[3]
# # # para limpiar todos los elemento de la lista se usa clear 
# # nombres.clear()
# # #eliminar lista por complete 
# # del nombres

#sintaxis de rango (inicio<opcional>, fin<requerido>, incremento,<opcional>)

#Ejercicio 1. Itera un rango de 0 a 10 imprimiendo numeros divisibles a 3

numeros=list(range(10))

for numero in numeros: # en lugar de la varible numeros se puede usar directo for in range(11)
    if numero%3==0:
        print(numero)

#Ejercicio 2. Crea un rango de numeros , e imprimelos

range2=list(range(2,7))
print(range2)

#Ejercicio 3. Crea un rango de 3 a 10, pero incrementa de 2 en 2

range3=list(range(3,11,2))
print(range3)

#contar cuantos elementos iguales hay en una lista 
lista = [1,2,3,1,2]
repeticiones = {}

for n in lista:
    if lista.count(n) != 1:
        if n in repeticiones :
            repeticiones[n] += 1
        else:
            repeticiones[n] = 0
print(repeticiones)


