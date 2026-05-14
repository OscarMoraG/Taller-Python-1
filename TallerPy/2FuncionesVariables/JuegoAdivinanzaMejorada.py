# Número secreto
numero = 50

# Variable global de intentos
intentos = 0


# Función para obtener el número secreto
def generar_numero():
    return numero


# Función para verificar adivinanza
def verificar_adivinanza(adivinanza):

    numero_secreto = generar_numero()

    if adivinanza == numero_secreto:
        return "correcto"

    elif adivinanza < numero_secreto:
        return "menor"

    else:
        return "mayor"


# Función para contar intentos
def contar_intento():

    global intentos
    intentos += 1


# Función para mostrar estadísticas
def mostrar_estadisticas():

    print("\n--- ESTADÍSTICAS ---")
    print("Número secreto:", numero)
    print("Cantidad de intentos:", intentos)


# Juego principal
def juego():

    while True:

        adivinanza = int(input("Digite un número entre 1 y 100: "))

        contar_intento()

        resultado = verificar_adivinanza(adivinanza)

        if resultado == "correcto":

            print("¡Adivinaste el número!")
            mostrar_estadisticas()
            break

        elif resultado == "menor":

            print("El número secreto es mayor")

        else:

            print("El número secreto es menor")


# Ejecutar juego
juego()