def main():
    import pickle
    print("Contactos")


    mascotas = open( "mascotas.txt", "r" )
    mascotas = mascotas.readlines()
    mascotas = [line.rstrip().split(',') for line in mascotas]
    choice = 0
    while choice != 4:
        print("\n Seleccione la opción correspondiente \n")
        print("1. Agregar Mascota")
        print("2. Buscar Mascota")
        print("3. Mostrar todas las mascotas")
        print("4. Quitar y guardar")
        choice = int(input())

        if choice == 1:
            print("Agregar una mascota")
            nombre = input("Agrega nombre de la mascota: ")
            owner = input("Agrega nombre del dueño: ")
            telefono = input("Agrega el teléfono del dueño: ")
            mascotas.append([nombre, owner, telefono])

        elif choice == 2:
            print("Busca una mascota")
            keyword = input("Escribe el término buscado: ")
            for mascota in mascotas:
                if keyword in mascota:
                    print(mascota)
        elif choice == 3:
            print("Mostrando todas las mascotas \n")
            for i in range(len(mascotas)):
                print(mascotas[i])
        elif choice == 4:
            print("Saliendo del programa")
        else:
            print("Respuesta inválida")

    pickle.dump(mascotas, pickle_file)
   
    ### Modifica hasta aquí
    cont = 0
    with open('mascotas.txt', 'w') as f:
        for m in mascotas:
            print(m)
            for p in m:
                cont += 1
                f.write(p)
                if cont != len(m):
                    f.write(',')
                elif cont == len(m):
                    f.write('\n')
            cont = 0
    
main()