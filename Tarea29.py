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
        monto = int(input("Monto a retirar: "))  # Usamos int en lugar de float
        if monto <= saldo:
            saldo -= monto
            print("Saldo actual:", saldo)
        else:
            print("Fondos insuficientes")
    elif opcion == "2":
        monto = int(input("Monto a depositar: "))  # Usamos int en lugar de float
        saldo += monto
        print("Saldo actual:", saldo)
    elif opcion != "3":
        print("Opción inválida")

#5 Calcular la raíz cuadrada por aproximación (método babilónico).

#6 Contar dígitos de un número entero (ej: 456 → 3).

#7 Generar la secuencia de Fibonacci hasta un límite.

#8 Encontrar números primos en un rango dado.

#9 Simular un temporizador (contar regresivamente desde N).

#10 Leer archivos línea por línea hasta fin de archivo.

# Mientras - While
#Visualizar los 5 primeros numeros con mientras - WHILE

contador = 0
while contador <= 10:
    print("Numero: ", contador)
    contador += 1
 