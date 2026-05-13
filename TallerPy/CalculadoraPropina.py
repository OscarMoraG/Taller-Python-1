# Solicitar datos
cuenta = float(input("Digite el valor de la cuenta: "))
porcentaje = float(input("Digite el porcentaje de propina: "))

# Calcular propina
propina = cuenta * (porcentaje / 100)

# Calcular total
total = cuenta + propina

# Mostrar resultados
print("----- FACTURA -----")
print("Valor de la cuenta:", round(cuenta, 2))
print("Porcentaje de propina:", porcentaje, "%")
print("Valor de la propina:", round(propina, 2))
print("Total a pagar:", round(total, 2))