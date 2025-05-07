# Proyecto 4: Juego de Adivinar el Número
numerosecreto = 5
intentos = 3

for i in range(intentos):
    intento = int(input(f"Intento {i+1}: Adivina el número (entre 1 y 10): "))
    
    if intento == numerosecreto:
        print("¡Correcto! Adivinaste el número.")
        break
    elif intento < numerosecreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")
else:
    print(f"Lo siento, no adivinaste el número. Era el {numerosecreto}.")
