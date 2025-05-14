import Pia_moduloavance as PIA
import os

def main():
    PIA.registrar()
    while True:
        os.system("clear")
        try:
            print("\tMENU PRINCIPAL")
            print("-" * 32)
            print(
                "Selecciona una opcion:\n1- Verificar dominios maliciosos\n2- Verificar links de Google maliciosos\n3- Importar datos desde la API\n4- Verificar datos acerca de (Url,domain,etc)\n5- Indicadores maliciosos iOs\n6-Salir"
            )
            print("-" * 32)
            opcion = int(input("\nOpcion: "))
            if opcion == 1:
                verificar_dominio()
            elif opcion == 2:
                verificar_link_google()
            elif opcion == 3:
                importar_datos()
            elif opcion == 4:
                verificar_malware()
            elif opcion == 5:
                verificar_datosiOs()
            elif opcion == 6:
                print("Gracias por usar el sistema. ¡Hasta luego!")
                PIA.registrar()
            else:
                input("Opción no válida")
        except:
            input("Debes ingresar un número")

def verificar_malware():
    os.system("clear")
    archivo_txt = "malware.txt"
    datos = PIA.cargar_datos_txt(archivo_txt)

    if datos:
        for dominio in datos:
            print(f"Tipo: {dominio['type']}, Dominio: {dominio['indicator']}")
    else:
        print("No se encontraron dominios maliciosos en el archivo TXT.")

    grafica = input("¿Desea ver la gráfica de frecuencia? (S/N): ")
    if grafica.lower() == "s":
        PIA.grafica_malware()
        input("\nPresiona ENTER para continuar...")

def verificar_dominio():
    os.system("clear")
    archivo_txt = "dominios_maliciosos.txt"
    datos = PIA.cargar_datos_txt(archivo_txt)

    if datos:
        for dominio in datos:
            print(f"Tipo: {dominio['type']}, Dominio: {dominio['indicator']}")
    else:
        print("No se encontraron dominios maliciosos en el archivo TXT.")

    grafica = input("¿Desea ver la gráfica de frecuencia? (S/N): ")
    if grafica.lower() == "s":
        PIA.graficar_dominios_maliciosos()
        input("\nPresiona ENTER para continuar...")
        

def verificar_link_google():
    os.system("clear")
    archivo_txt = "google_links_maliciosos.txt"
    datos = PIA.cargar_datos_txt(archivo_txt)

    if datos:
        for link in datos:
            print(f"Tipo: {link['type']}, Link: {link['indicator']}")
    else:
        print("No se encontraron links maliciosos en el archivo TXT.")

    grafica = input("¿Desea ver la gráfica de frecuencia? (S/N): ")
    if grafica.lower() == "s":
        PIA.graficar_links_maliciosos()
        input("\nPresiona ENTER para continuar...")
