# Lista global para guardar notas
notas = []


# Función para agregar nota
def agregar_nota(nota):
    notas.append(nota)
    print("Nota agregada correctamente")


# Función para calcular promedio
def calcular_promedio():

    if len(notas) == 0:
        return 0

    promedio = sum(notas) / len(notas)
    return promedio


# Función para contar notas
def contar_notas():
    return len(notas)


# Función para reiniciar sistema
def reset_notas():
    notas.clear()
    print("Sistema reiniciado")


# Función para mostrar estado
def mostrar_estado():

    print("\n--- ESTADO DEL SISTEMA ---")

    print("Notas registradas:", notas)

    print("Cantidad de notas:", contar_notas())

    print("Promedio:", round(calcular_promedio(), 2))


# Menú principal
def menu():

    while True:

        print("\n--- MENÚ ---")
        print("1. Agregar nota")
        print("2. Calcular promedio")
        print("3. Contar notas")
        print("4. Reiniciar sistema")
        print("5. Mostrar estado")
        print("6. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:

            nota = float(input("Digite la nota: "))
            agregar_nota(nota)

        elif opcion == 2:

            print("Promedio:", round(calcular_promedio(), 2))

        elif opcion == 3:

            print("Cantidad de notas:", contar_notas())

        elif opcion == 4:

            reset_notas()

        elif opcion == 5:

            mostrar_estado()

        elif opcion == 6:

            print("Programa finalizado")
            break

        else:

            print("Opción no válida")


# Ejecutar menú
menu()