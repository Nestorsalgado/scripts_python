#realiza un programa que pregunte al usuario  cuantos numeros quiere ingresar. Luego debe leer todos los numeros y obtener la media aritmetica 
# la sumatoria de todos los numeros entre la suma de la cantidad de numeros
cant_num = int(input("¿C'uantos n'umeros deseas ingresar?\n\t"))
suma=0

for e in range (cant_num):
    suma += float(input("numero"))
media=cant_num /suma
print(f"\n Se han introducido {cant_num} n'umeros que en total suman {suma}. \n La media aritmetica es {cant_num /suma}" )
