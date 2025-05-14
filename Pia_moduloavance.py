def cargar_datos_txt(nombre_archivo):
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            try:
                return json.load(archivo)  # Cargar como un objeto JSON completo
            except json.JSONDecodeError:
                return []
    return []

def guardar_datos_txt(nuevos_datos, nombre_archivo):
    datos_guardados = cargar_datos_txt(nombre_archivo)
    indicadores_existentes = {item["indicator"] for item in datos_guardados}

    nuevos_unicos = [
        {
            "type": item["type"],
            "indicator": item["indicator"],
            "created": item["created"],
            "pulse_key": item["pulse_key"],
            "id": item["id"]
        }
        for item in nuevos_datos
        if item["indicator"] not in indicadores_existentes
    ]

    datos_guardados.extend(nuevos_unicos)

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos_guardados, archivo, indent=4, ensure_ascii=False)

    print(f"Se han guardado correctamente {len(nuevos_unicos)} nuevos indicadores en {nombre_archivo}.")

# -------------------------
# Usuarios
# -------------------------

def registrar():
    while True:
        os.system("clear")
        try:
            print("-" * 32)
            print("1- Iniciar sesion\n2- Registrarse\n3- Salir")
            print("-" * 32)
            menu = int(input("\nOpcion: "))
            if menu == 1:
                valid = ingresar_usuario()
                if valid == True:
                    break
            elif menu == 2:
                registrar_usuario()
            elif menu == 3:
                input("Gracias por usar el programa.")
                os.system("close()")
            else:
                input("Opción no válida")
        except:
            input("Debes ingresar un número")

def ingresar_usuario():
    valid = False
    while True:
        os.system("clear")
        correo = input("Ingrese su correo electrónico: \n")
        contraseña = input("Ingrese su contraseña: \n")
        if verificar_usuario(correo, contraseña):
            input("Inicio de sesión exitoso.")
            valid = True
            break
        else:
            input("Correo o contraseña incorrectos. Intente nuevamente.")
            break
    return valid


def registrar_usuario():
    while True:
        os.system("clear")
        correo = input("Ingrese su correo electrónico de registro: \n")
        if not validar_correo(correo):
            input(
                "El correo no es válido. Debe seguir el formato usuario@mail.com. Intente nuevamente."
            )
        else:
            break

    while True:
        contraseña = input("Ingrese su contraseña de registro: \n")
        if not validar_contraseña(contraseña):
            input(
                "La contraseña debe contener al menos una mayúscula y un número. Intente nuevamente."
            )
        else:
            break

    if guardar_usuario(correo, contraseña):
        input("Usuario registrado exitosamente.")
    else:
        input("El correo ya está registrado. Intente con otro correo.")

def guardar_usuario(correo, contrasena):
    datos = []

    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r", encoding="utf-8") as archivo:
            try:
                datos = json.load(archivo)
            except:
                datos = []
        for usuario in datos:
            if usuario["correo"] == correo:
                return False
            
    datos.append({
        "correo": correo,
        "contrasena": contrasena
    })
    with open("usuarios.txt", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4)
    return True

def verificar_usuario(correo, contrasena):
    if not os.path.exists("usuarios.txt"):
        return False

    with open("usuarios.txt", "r", encoding="utf-8") as archivo:
        try:
            datos = json.load(archivo)
        except:
            return False  
    for usuario in datos:
        if usuario["correo"] == correo and usuario["contrasena"] == contrasena:
            return True  
    return False


def validar_correo(correo):
    return re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', correo)

def validar_contraseña(contrasena):
    return re.match(r'^(?=.*[A-Z])(?=.*\d).+$', contrasena)