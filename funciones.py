# # bloque de codigo para llamar n veces

# def mi_funcion():
#     print("Practicando ando ")



# #llamada 
# #x1
# mi_funcion()
# #x2
# mi_funcion()

# #paso de argumentos los argumentos son las variables que pasamos a nuestra funcion 

# def mi_funcion(nombre):
#     print( f"Hola pedro  {nombre} ")

# #llamada 
# #x1
# mi_funcion("pedro")
# mi_funcion("sofia")

#funcion con return 

# def suma(a,b):  \\ para agregar valor por defecto def suma(a=0,b=5)
#     resulatdo=a+b
#     return resulatdo

# # print(suma(5,8))
# # total=suma(5,8)
# # print(f"El resultado sumar es:{total}")
# print(f"El resultado sumar es:{suma(5,8)}")

# # pasar argumentos variables en una funcion 

# def lista_nombres(*nombres):  # args como no conocemos el numero de elementos a pasar, el asterisco combierte los datos en una tupla 
#     for nombre in nombres:
#         print(nombre)

# lista_nombres("juan","pedro","maria", "nestor") 
# #___________________________________________________________________________________________________
# """Crea una función para sumar los valores recibidos de tipo numerico,
# utilizando argumentos variables *args como parametro de la función
# y regresando como resultado la suma de todos los valores pasados como argumendos """

# def sumar(*num):
#     total=0
#     for i in num:
#         total +=i
#     return total

# print(sumar(3,5,9))

# """crear una funcion para multiplicar los valores recibidos de tipo nuérico, utilizando argumentos variables de la función
# y regresar como resultado la multiplicación de todos los valores pasados como argumentos"""

# def multiplica_valores(*num):
#     total=1
#     for i in num:
#         total *=i
#     return total

# print(multiplica_valores(1,2,3))

# #funcion que maneja kwargs llave valor

# def listaTerminos(**lt):
#     for llave, valor in lt.items():
#         print(f"{llave}:{valor}")

# listaTerminos(IDE="ide")

# """funcion recursiva factorial 5!=5*4*3*2*1"""

# def factorial(num):
#     if num==1:
#         return 1
#     else:
#         return num * factorial(num-1)

# print(factorial(5))


def descendente(des):
    if des >=1:

    
        print(des)
        return descendente(des-1)
    elif des ==0 :
        print("El valos es negativo")
        
    
        

descendente(5)










