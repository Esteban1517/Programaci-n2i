#proyecto 3: Tabla de multiplicar personalizada 
x= int(input("Ingrese un número: "))
print(f"Tabla de multiplicar del {x}: ")
for i in range(1,13):
    producto=i*x
    print(f"producto",i , "x", x ,"=", producto)