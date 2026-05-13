# Solicitar datos al usuario
peso = float(input("Digite su peso en kilogramos: "))
altura = float(input("Digite su altura en metros: "))

# Calcular el IMC
imc = peso / (altura ** 2)

# Mostrar el resultado con 2 decimales
print("Su IMC es:", round(imc, 2))

# Clasificación del IMC
if imc < 18.5:
    print("Bajo peso")

elif imc < 25:
    print("Peso normal")

elif imc < 30:
    print("Sobrepeso")

else:
    print("Obesidad")