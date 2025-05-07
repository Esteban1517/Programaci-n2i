# PROYECTO5
Alumno=input("Ingresa tu nombre: ")
suma=0

for sum in range(4):
    
    Calificaciones=int(input(f"Ingresa tus calificaciones  {sum +1} entre 0 a 20= "))

    suma += Calificaciones

    promedio=suma/4

print(f"Tu promedio es {promedio} ")

if promedio > 14:
    print(f"{Alumno}, tu proemdio es de {promedio}, felicitaciones aprobaste")

else:
    print(f"lo siento {Alumno}, reprobaste, nos vemos el siguiente año")