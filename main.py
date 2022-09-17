from datetime import date

print("Menu")
print("1.Nombre y año de nacimiento")
print("2.calcular edad")
print("3.SALUDO DE BUENAS NOCHES")
print("4.AÑOS EN 2030")
print("5.SALIR")

opcion = 100

while(opcion != 5):
    if(opcion == 1):
        nombre=input("Digite Su nombre")
        anoNacimiento=int(input("Digite su año de nacimiento"))
    elif(opcion == 2):
        anoNacimiento=int(input("Digite su año de nacimiento"))
        print(f"Su edad es "+int(2022-anoNacimiento))

else:
    print("Digite una opcion correcta")

