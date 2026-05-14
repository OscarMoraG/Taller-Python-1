# Diccionario del inventario
inventario = {}


# Función para agregar productos
def agregar_producto():

    nombre = input("Digite el nombre del producto: ")
    cantidad = int(input("Digite la cantidad: "))

    inventario[nombre] = cantidad

    print("Producto agregado correctamente")


# Función para buscar productos
def buscar_producto():

    nombre = input("Digite el producto a buscar: ")

    if nombre in inventario:

        print("Producto encontrado")
        print("Cantidad disponible:", inventario[nombre])

    else:

        print("El producto no existe")


# Función para actualizar cantidades
def actualizar_cantidad():

    nombre = input("Digite el producto a actualizar: ")

    if nombre in inventario:

        nueva_cantidad = int(input("Digite la nueva cantidad: "))

        inventario[nombre] = nueva_cantidad

        print("Cantidad actualizada")

    else:

        print("El producto no existe")


# Función para mostrar inventario
def mostrar_inventario():

    print("\n--- INVENTARIO COMPLETO ---")

    for producto, cantidad in inventario.items():

        print(producto, ":", cantidad)


# Función para mostrar stock bajo
def stock_bajo():

    print("\n--- PRODUCTOS CON STOCK BAJO ---")

    for producto, cantidad in inventario.items():

        if cantidad < 5:

            print(producto, ":", cantidad)


# Menú principal
def menu():

    while True:

        print("\n--- MENÚ ---")
        print("1. Agregar producto")
        print("2. Buscar producto")
        print("3. Actualizar cantidad")
        print("4. Mostrar inventario")
        print("5. Mostrar stock bajo")
        print("6. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:

            agregar_producto()

        elif opcion == 2:

            buscar_producto()

        elif opcion == 3:

            actualizar_cantidad()

        elif opcion == 4:

            mostrar_inventario()

        elif opcion == 5:

            stock_bajo()

        elif opcion == 6:

            print("Programa finalizado")
            break

        else:

            print("Opción no válida")


# Ejecutar menú
menu()