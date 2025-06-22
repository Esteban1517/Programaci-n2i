#Ejercicio 1
frutas = ["carro", "moto", "bicicleta", "avion", "barco"]
# Recorremos la lista con enumerate para obtener índice y valor
for indice, fruta in enumerate(frutas):
    print(f"Índice {indice}: {fruta}")


#Ejercicio 2
palabras = input("Ingresa varias palabras separadas por espacios: ").split()
# Usamos max con key=len para encontrar la palabra más larga
palabra_larga = max(palabras, key=len)
print("La palabra más larga es:", palabra_larga)


#Ejercicio 3
linea = input("Escribe una línea de texto: ")
palabras = linea.split()

frecuencia = {}

for palabra in palabras:
    palabra = palabra.lower()  
    frecuencia[palabra] = frecuencia.get(palabra, 0) + 1

print("Frecuencia de palabras:")
for palabra, conteo in frecuencia.items():
    print(f"{palabra}: {conteo}")


#Ejercicio 4
from collections import Counter
try:
    with open("datos.txt", "r", encoding="utf-8") as archivo:
        texto = archivo.read().lower().split()

    conteo = Counter(texto)
    mas_comunes = conteo.most_common(3)

    print("Las 3 palabras más repetidas son:")
    for palabra, frecuencia in mas_comunes:
        print(f"{palabra}: {frecuencia} veces")
except FileNotFoundError:
    print("El archivo 'datos.txt' no fue encontrado.")


#Ejercicio 5
tienda = {
    "pan": 0.50,
    "leche": 1.20,
    "huevos": 2.00,
    "arroz": 1.00,
    "azúcar": 0.90
}
print("Bienvenido a la tienda. Productos disponibles:")
for producto, precio in tienda.items():
    print(f"{producto}: ${precio:.2f}")
# Buscar un producto
busqueda = input("¿Qué producto desea buscar?: ").lower()
if busqueda in tienda:
    print(f"{busqueda} cuesta ${tienda[busqueda]:.2f}")
else:
    print("Producto no encontrado.")