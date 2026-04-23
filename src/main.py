from service import crear_registro, listar_registros

def main():
    print("============ SISTEMA GESTION INFO ===============")

    while True:
        print("1. Crear registro")
        print("2. Listar registros")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("------ CREAR REGISTRO ------")
            id = input("Ingrese ID: ")
            nombre = input("Ingrese nombre: ")
            correo = input("Ingrese correo: ")

            print(crear_registro(id, nombre, correo))

        elif opcion == "2":
            print("------ LISTA DE REGISTROS ------")
            listar_registros()


        elif opcion == "3":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida\n")

if __name__ == "__main__":
    main()