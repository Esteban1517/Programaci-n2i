# PROYECTO #1 
Usuario=input("Cual es su nombre: ")
Año=int(input("Ingresa tu año de nacimiento= "))

añoactual=2025

EdadAprox=añoactual-Año

print(f"Hola {Usuario}, tienes aproximadamente {EdadAprox} años")

if EdadAprox > 18:
    print("Eres mayor de edad")

else:
    print("No eres mayor de edad")

