#1 Sumar números ingresados por el usuario hasta que ingrese 0.
suma = 0
numero = int(input("Ingresa un número (0 para terminar): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingresa otro número (0 para terminar): "))

print("La suma es:", suma)

#2 Adivinar un número aleatorio entre 1 y 100 (pistas: "mayor" o "menor").
secreto = 69  
intento = int(input("Adivina el número (1-100): "))

while intento != secreto:
    if intento < secreto:
        print("Mayor")
    else:
        print("Menor")
    intento = int(input("Intenta de nuevo: "))

print("¡Correcto!")

#3 Validar contraseña (repetir hasta que coincida con una guardada).
clavecorrecta = "123"                     
clave = input("Introduce la contraseña: ") 

while clave != clavecorrecta:             
    print("Contraseña incorrecta")         
    clave = input("Intenta otra vez: ")    

print("Contraseña correcta")               

#4 Simular un cajero automático (menú: retirar, depositar, salir).

saldo = 1000
opcion = ""

while opcion != "3":
    print("MENU\n 1. Retirar\n 2. Depositar\n 3. Salir")
    opcion = input("Elige opción: ")

    if opcion == "1":
        monto = int(input("Monto a retirar: "))  
        if monto <= saldo:
            saldo -= monto
            print("Saldo actual:", saldo)
        else:
            print("Fondos insuficientes")
    elif opcion == "2":
        monto = int(input("Monto a depositar: "))  
        saldo += monto
        print("Saldo actual:", saldo)
    elif opcion != "3":
        print("Opción inválida")

#5 Calcular la raíz cuadrada por aproximación (método babilónico).
n = int(input("Número: "))
x = n
tolerancia = 1
raiz = (x + n // x) // 2

diferencia = raiz - x
if diferencia < 0:
    diferencia = -diferencia

while diferencia >= tolerancia:
    x = raiz
    raiz = (x + n // x) // 2

    diferencia = raiz - x
    if diferencia < 0:
        diferencia = -diferencia

print("Raíz cuadrada aproximada:", raiz)

#6 Contar dígitos de un número entero (ej: 456 → 3).
numero = int(input("Número entero: "))
contador = 0

if numero < 0:
    numero = -numero  # convierte a positivo sin usar abs

if numero == 0:
    contador = 1
else:
    while numero > 0:
        numero = numero // 10
        contador += 1

print("Cantidad de dígitos:", contador)

#7 Generar la secuencia de Fibonacci hasta un límite.
limite = int(input("Ingresa el límite: "))
a, b = 0, 1

while a <= limite:
    print(a, end=" ")
    a, b = b, a + b

#8 Encontrar números primos en un rango dado.
inicio = int(input("\nInicio del rango de numeros primos: "))
fin = int(input("Fin del rango: "))

for num in range(inicio, fin + 1):
    if num > 1:
        es_primo = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                es_primo = False
        if es_primo:
            print(num, end=" ")

#9 Simular un temporizador (contar regresivamente desde N).
n = int(input("\nIngresa el número inicial del temporizador: "))

while n >= 0:
    print(n)
    n -= 1

print("¡Tiempo terminado!")

#10 Leer archivos línea por línea hasta fin de archivo.
archivo_nombre = input("Nombre del archivo: ")

archivo = open(archivo_nombre, "r")
linea = archivo.readline()
while linea != "":
    print(linea.strip())
    linea = archivo.readline()
archivo.close()


# Mientras - While
#Visualizar los 5 primeros numeros con mientras - WHILE

contador = 0
while contador <= 10:
    print("Numero: ", contador)
    contador += 1
 