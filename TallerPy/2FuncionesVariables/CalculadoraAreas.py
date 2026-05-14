# Función para área del cuadrado
def area_cuadrado():
    lado = float(input("Digite el lado del cuadrado: "))
    area = lado ** 2
    print("El área del cuadrado es:", round(area, 2))


# Función para área del rectángulo
def area_rectangulo():
    base = float(input("Digite la base: "))
    altura = float(input("Digite la altura: "))
    area = base * altura
    print("El área del rectángulo es:", round(area, 2))


# Función para área del triángulo
def area_triangulo():
    base = float(input("Digite la base: "))
    altura = float(input("Digite la altura: "))
    area = (base * altura) / 2
    print("El área del triángulo es:", round(area, 2))


# Función para área del círculo
def area_circulo():
    radio = float(input("Digite el radio: "))
    pi = 3.14159
    area = pi * (radio ** 2)
    print("El área del círculo es:", round(area, 2))


# Menú principal
def menu():
    print("--- MENÚ ---")
    print("1. Área del cuadrado")
    print("2. Área del rectángulo")
    print("3. Área del triángulo")
    print("4. Área del círculo")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        area_cuadrado()

    elif opcion == 2:
        area_rectangulo()

    elif opcion == 3:
        area_triangulo()

    elif opcion == 4:
        area_circulo()

    else:
        print("Opción no válida")


# Ejecutar menú
menu()