
### Loops ###

# While

mi_condicion = 0

while mi_condicion < 10:
    print(mi_condicion)
    mi_condicion += 2
else:  # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continúa")

while mi_condicion < 20:
    mi_condicion += 1
    if mi_condicion == 15:
        print("Se detiene la ejecución")
        break
    print(mi_condicion)

print("La ejecución continúa")

# For

mi_lista = [18, 24, 62, 52, 30, 30, 17]

for element in mi_lista:
    print(element)

mi_tuple = (18, 1.77, "Hernan", "Cordoba", "Hernan")

for element in mi_tuple:
    print(element)

mi_set = {"Hernan", "Cordoba", 18}

for element in mi_set:
    print(element)

mi_diccionario = {"Nombre": "Hernan", "Apellido": "Cordoba", "Edad": 18, 1: "Python"}

for element in mi_diccionario:
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para el diccionario ha finalizado")

print("La ejecución continúa")

for element in mi_diccionario:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")