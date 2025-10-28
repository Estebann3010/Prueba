# Programa Vacunatorio 
genero_contador = {"M": 0, "F": 0, "O": 0}
mujeres_mayores_60 = 0
menor_12_vacunado = 0

while True:
    genero = input("Ingrese genero (M/F/O, fin para salir): ").upper()
    if genero not in ["M", "F", "O"]:
        break
    try:
        edad = int(input("Ingrese edad: "))
    except ValueError:
        print("Edad invalida. Intente de nuevo.")
        continue

    genero_contador[genero] += 1

    if genero == "F" and edad >= 60:
        mujeres_mayores_60 += 1
    if edad <= 12:
        menor_12_vacunado += 1

genero_mayor = max(genero_contador, key=genero_contador.get)
genero_nombre = {"M": "Masculino", "F": "Femenino", "O": "Otro"}

print("-----------------------------------------------------------------------")
print(f"El genero con mayor cantidad de personas vacunadas es: {genero_nombre[genero_mayor]}")
print(f"Cantidad de mujeres mayores de 60 anios vacunadas: {mujeres_mayores_60}")
print("-----------------------------------------------------------------------")
if menor_12_vacunado > 0:
    print("-----------------------------------------------------------------------")
    print("Si se han vacunado a persona/s de 12 anios.")
    print(f"Cantidad de personas menores de 12 anios vacunadas: {menor_12_vacunado}")
    print("-----------------------------------------------------------------------")
else:
    print("-----------------------------------------------------------------------")
    print("No se han vacunado a persona/s de 12 anios.")
    print("-----------------------------------------------------------------------")