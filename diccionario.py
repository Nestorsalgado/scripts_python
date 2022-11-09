# lave: valor

diccionario={
    "IDE": "Integrated Development Environment",
    "OOP":"Object Oriented Programing",
    "DBMS": "Database Managenment System",
    "MODIFICAR":"TAL"
}

print(diccionario)
# largo de diccionario
print(len(diccionario))
#no hay indices para entrar a un elemento hay que usar (key)
print(diccionario["IDE"])
print(diccionario.get("OOP")) #ESTA ES OTRA MANERA 
#PARA MODIFICAR 
diccionario["MODIFICAR"]="TALCUAL"
print(diccionario["MODIFICAR"])
#recorrer elemento de un diccionario
for key in diccionario:
    print(key)

#para acceder al valor usamos la palabra items():

for key, valor in diccionario.items():
    print(key, valor)
# unicamente llaves
for key in diccionario.keys():
    print(key)
#unicamente valores 
for valor in diccionario.values():
    print(valor)

#comprobar si existe elemento 
print("IDE" in diccionario)
#agregar elemento en diccionario 
diccionario["PK"]="Primary Key "
print(diccionario) #en caso de que ya exista, sobre escribe el valor 
#remover
diccionario.pop("MODIFICAR")
#limpiar diccionario 
diccionario.clear()
#eliminar por completo 
del diccionario



