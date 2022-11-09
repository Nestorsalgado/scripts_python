# programa que lea un numero del 0 al 9, mientras que no sea correcto se repita el proceso, luego debe comprobar si el numero se encuentra en la lista de
#numeros [0,1,3,5,8] y notificar 


lista=[0,1,3,5,8]

while(True):
    numero= int(input("Introdusca un numero entre 0 y 9\n"))
    if numero >= 0 and numero <= 9:
        break

if numero in lista:
    print(f"El numero {numero} se encuentra en la lista {lista}")
else:
    print("el numero no esta")