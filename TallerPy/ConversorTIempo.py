# Solicitar minutos
minutos = int(input("Digite la cantidad de minutos: "))

# Calcular horas
horas = minutos // 60

# Calcular minutos restantes
minutos_restantes = minutos % 60

# Mostrar resultado
print(minutos, "minutos equivalen a", horas, "horas y", minutos_restantes, "minutos")