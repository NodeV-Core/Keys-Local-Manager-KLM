import json 
import time

def get_account():
    print("Ha ingresado al sistema de guardado de claves, por favor, espere un momento...")
    time.sleep(2)
    servicio = input("Ingrese el servicio al cual pertenece su clave: ")
    correo = input("Ingrese el correo que posee su cuenta: ")
    clave = input("Ingrese la clave de su correo o servicio: ")

    user_data = {
        "Servicio": servicio,
        "Correo": correo,
        "Contraseña": clave
    }
    return user_data 

def save_new_account(new_account):
    try:
        with open("keys.json", "r") as file:
            available_accounts = json.load(file)
    except FileNotFoundError:
        available_accounts = []
    available_accounts.append(new_account)
    with open("keys.json", "w") as file:
        json.dump(available_accounts, file, indent=4)

def show_accounts():
    print("===============")
    print("# Mis Cuentas #")
    print("===============")

    try:
        with open("keys.json", "r") as file:
            accounts = json.load(file)

        for account in accounts:
            print(f"Servicio: {account['Servicio']}")
            print(f"Correo: {account['Correo']}")
            print(f"Contraseña: {account['Contraseña']}")

    except FileNotFoundError:
        print("Parece que aún no has guardado ninguna cuenta")

while True:
    print("========================================================")
    print("Bienvenido a nuetro sistema de guardado local de cuentas")
    print("========================================================")

    print('\n'"Por favor selecciona el procedimiento que deseas llevar")
    print("[1] - Guardar Nueva Cuenta")
    print("[2] - Visualizar Cuentas Guardadas")
    print("[3] - Salir del sistema")
    selection = int(input("~# "))    

    if selection == 1:
        new_account = get_account()
        save_new_account(new_account)
    elif selection == 2:
        show_accounts()
        time.sleep(10)
        print('\n')
    elif selection == 3:
        print("Saliendo del sistema.")
        time.sleep(0.3)
        print("Saliendo del sistema..")
        time.sleep(0.3)
        print("Saliendo del sistema...")
        time.sleep(0.3)
        break
    else:
        print('\n'"Lo sentimos pero su eleccion no fue valida, por favor vuelva a intentarlo")