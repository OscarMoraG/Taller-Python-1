# Función metros
def convertir_metros():

    metros = float(input("Digite los metros: "))

    centimetros = metros * 100
    kilometros = metros / 1000

    print("Centímetros:", centimetros)
    print("Kilómetros:", kilometros)


# Función kilos
def convertir_kilos():

    kilos = float(input("Digite los kilos: "))

    gramos = kilos * 1000
    libras = kilos * 2.20462

    print("Gramos:", gramos)
    print("Libras:", round(libras, 2))


# Función horas
def convertir_horas():

    horas = float(input("Digite las horas: "))

    minutos = horas * 60
    segundos = horas * 3600

    print("Minutos:", minutos)
    print("Segundos:", segundos)


# Menú principal
def menu():

    while True:

        print("--- MENÚ PRINCIPAL ---")
        print("1. Convertir metros")
        print("2. Convertir kilos")
        print("3. Convertir horas")
        print("4. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:

            convertir_metros()

        elif opcion == 2:

            convertir_kilos()

        elif opcion == 3:

            convertir_horas()

        elif opcion == 4:

            print("Programa finalizado")
            break

        else:

            print("Opción no válida")


# Ejecutar menú
menu()