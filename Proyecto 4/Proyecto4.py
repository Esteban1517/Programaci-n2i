# Proyecto 4: Juego de Adivinar el Número
numero_secreto = 5
intentos = 3

for i in range(intentos):
    intento = int(input(f"Intento {i+1}: Adivina el número (entre 1 y 10): "))
    
    if intento == numero_secreto:
        print("¡Correcto! Adivinaste el número.")
        break
    elif intento < numero_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")
else:
    print(f"Lo siento, no adivinaste el número. Era el {numero_secreto}.")
