#a estos los diferencia que no mantienen un orden en indice, no se pueden modificar elelmentos, se pueden agregar y eliminar 
# en este caso se usan{llaves} para definir

planetas={"marte","venus","tierra"}
#al imprimir no se imprimen en el mismop orde
print(planetas)
# largo de los elementos 
print(len(planetas))
#revisar si un elemento esta presente // esta misma es aplicable en listas y tuplas 
print("marte" in planetas)
#para agregar un elemento
planetas.add("jupiter")
# no soporta elementos duplicados 

#eliminamos elementos con remove este metodo marca error en caso de no encontrarse 
planetas.remove("tierra")
#eliminamos elementos con discard en este caso si no se encuentra no marca error
planetas.discard("tierras")
#limpiar set por completo
planetas.clear()
#eliminar por completo el set 
del planetas
