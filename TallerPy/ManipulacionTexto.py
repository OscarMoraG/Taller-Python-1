# Solicitar frase
frase = input("Digite una frase: ")

# Convertir texto
print("Mayúsculas:", frase.upper())
print("Minúsculas:", frase.lower())

# Separar palabras
palabras = frase.split()

# Cantidad de palabras
print("Número de palabras:", len(palabras))

# Primera palabra
print("Primera palabra:", palabras[0])

# Última palabra
print("Última palabra:", palabras[-1])