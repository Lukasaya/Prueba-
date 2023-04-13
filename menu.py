import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_user():
    while True:
        username = input("Ingrese nombre de usuario a crear: ")
        if os.path.exists("/home/" + username):
            print("Error: El usuario ya existe")
        else:
            os.system("useradd " + username)
            print("Usuario creado exitosamente")
            break

def delete_user():
    while True:
        username = input("Ingrese nombre de usuario a eliminar: ")
        if not os.path.exists("/home/" + username):
            print("Error: El usuario no existe")
        else:
            os.system("userdel -r " + username)
            print("Usuario eliminado exitosamente")
            break

def create_file():
    while True:
        filename = input("Ingrese nombre de archivo a crear: ")
        if os.path.exists(filename):
            print("Error: El archivo ya existe")
        else:
            os.system("touch " + filename)
            print("Archivo creado exitosamente")
            break

def delete_file():
    while True:
        filename = input("Ingrese nombre de archivo a eliminar: ")
        if not os.path.exists(filename):
            print("Error: El archivo no existe")
        else:
            os.system("rm " + filename)
            print("Archivo eliminado exitosamente")
            break

while True:
    clear_screen()
    print("========BIENVENIDO ADMIN LINUX========")
    print("a.- Administración de usuarios")
    print("b.- Administración de archivos")
    print("c.- Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == 'a':
        while True:
            clear_screen()
            print("========ADMIN USUARIOS========")
            print("a.- Crear usuario")
            print("b.- Eliminar usuario")
            print("c.- Volver")

            subopcion = input("Seleccione una opción: ")

            if subopcion == 'a':
                create_user()
                input("Presione ENTER para regresar al menú de usuarios")
            elif subopcion == 'b':
                delete_user()
                input("Presione ENTER para regresar al menú de usuarios")
            elif subopcion == 'c':
                break
            else:
                input("Opción no válida. Presione ENTER para intentarlo de nuevo")

    elif opcion == 'b':
        while True:
            clear_screen()
            print("========ADMIN ARCHIVOS========")
            print("a.- Crear archivo")
            print("b.- Eliminar archivo")
            print("c.- Volver")

            subopcion = input("Seleccione una opción: ")

            if subopcion == 'a':
                create_file()
                input("Presione ENTER para regresar al menú de archivos")
            elif subopcion == 'b':
                delete_file()
                input("Presione ENTER para regresar al menú de archivos")
            elif subopcion == 'c':
                break
            else:
                input("Opción no válida. Presione ENTER para intentarlo de nuevo")

    elif opcion == 'c':
        clear_screen()
        print("Saliendo...")
        break

    else:
        input("Opción no válida. Presione ENTER para intentarlo de nuevo")
