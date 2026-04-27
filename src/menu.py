from service import new_register, list_records, search_record, update_record, delete_record
from colorama import Fore, Back, init 

init(autoreset=True)

def menu():
    print(Fore.GREEN + "============ SISTEMA GESTION INFO ===============")

    while True:
        print(Fore.BLUE + "\n1. Crear registro")
        print(Fore.RED + "2. Listar registros")
        print(Fore.YELLOW + "3. Buscar registros")
        print(Fore.MAGENTA + "4. Actualizar registros")
        print(Fore.CYAN + "5. Eliminar registros")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print(Back.BLUE + "\n------ CREAR REGISTRO ------")
            id = input("Ingrese ID: ")
            nombre = input("Ingrese nombre: ")
            correo = input("Ingrese correo: ")

            print(new_register(id, nombre, correo))

        elif opcion == "2":
            print(Back.RED + "\n------ LISTA DE REGISTROS ------")
            list_records()


        elif opcion == "3":
            print(Back.YELLOW + "\n------ BUSCAR REGISTRO ------")
            id = input("Ingrese ID a buscar: ")

            resultado = search_record(id)
            print(resultado)

        elif opcion == "4":
            print(Back.MAGENTA + "\n------ ACTUALIZAR REGISTRO ------")
            id = input("Ingrese ID a actualizar: ")
            nombre = input("Nuevo nombre (dejar vacío si no cambia): ")
            correo = input("Nuevo correo (dejar vacío si no cambia): ")

            print(update_record(id, nombre or None, correo or None))

        elif opcion == "5":
            print(Back.CYAN + "\n------ ELIMINAR REGISTRO ------")
            id = input("Ingrese ID a eliminar: ")

            print(delete_record(id))

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")