# Variable global
productos_disponibles = 100


# Función para vender productos
def vender_producto(cantidad):

    global productos_disponibles

    if cantidad <= productos_disponibles:

        productos_disponibles -= cantidad
        print("Venta realizada correctamente")

    else:

        print("No hay suficientes productos")


# Función para reabastecer inventario
def reabastecer(cantidad):

    global productos_disponibles

    productos_disponibles += cantidad

    print("Inventario actualizado")


# Función para consultar inventario
def consultar_inventario():

    print("Productos disponibles:", productos_disponibles)


# Función para verificar inventario bajo
def inventario_bajo():

    return productos_disponibles < 10


# Función para mostrar reporte
def reporte_inventario():

    print("\n--- REPORTE INVENTARIO ---")

    print("Productos disponibles:", productos_disponibles)

    print("¿Inventario bajo?:", inventario_bajo())


# Menú principal
def menu():

    while True:

        print("\n--- MENÚ ---")
        print("1. Vender producto")
        print("2. Reabastecer inventario")
        print("3. Consultar inventario")
        print("4. Reporte inventario")
        print("5. Salir")

        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:

            cantidad = int(input("Cantidad a vender: "))
            vender_producto(cantidad)

        elif opcion == 2:

            cantidad = int(input("Cantidad a agregar: "))
            reabastecer(cantidad)

        elif opcion == 3:

            consultar_inventario()

        elif opcion == 4:

            reporte_inventario()

        elif opcion == 5:

            print("Programa finalizado")
            break

        else:

            print("Opción no válida")


# Ejecutar menú
menu()