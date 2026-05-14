# Solicitar datos
producto = input("Digite el nombre del producto: ")
precio = float(input("Digite el precio unitario: "))
cantidad = int(input("Digite la cantidad a comprar: "))

# Calcular subtotal
subtotal = precio * cantidad

# Calcular IVA
iva = subtotal * 0.19

# Calcular total
total = subtotal + iva

# Mostrar resultados
print("----- FACTURA -----")
print("Producto:", producto)
print("Subtotal:", round(subtotal, 2))
print("IVA:", round(iva, 2))
print("Total a pagar:", round(total, 2))