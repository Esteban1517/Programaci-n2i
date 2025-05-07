# Contador de Vocales

# 1. Pedir al usuario que escriba una frase o palabra
frase = input("Escribe una frase o palabra: ")

frase=frase.lower()

# 2. Inicializar un diccionario para contar las vocales
vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# 3. Recorrer la cadena y contar las vocales
for letra in frase:
    if letra in vocales:
        vocales[letra] += 1

# 4. Mostrar los resultados
print("\nCantidad de cada vocal:")
for vocal, cantidad in vocales.items():
    print(f"{vocal}: {cantidad}")
