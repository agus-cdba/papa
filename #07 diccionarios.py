# Clase en vídeo: https://youtu.be/Kp4Mvapo5kc

### Dictionaries ###

# Definición

mi_diccionario = dict()
mi_otro_diccionario= {}

print(type(mi_diccionario))
print(type(mi_otro_diccionario))

mi_otro_diccionario = {"Nombre": "milanesa",
                 "Apellido": "con papas", "Edad": 25, 1: "Python"}

mi_diccionario = {
    "Nombre": "hernan",
    "Apellido": "cordoba",
    "Edad": 18,
    "Lenguajes": {"Python", "algo de ingles", "español"},
    1: 1.77
}

print(mi_otro_diccionario)
print(mi_diccionario)

print(len(mi_otro_diccionario))
print(len(mi_diccionario))

# Búsqueda

print(mi_diccionario[1])
print(mi_diccionario["Nombre"])

print("hernan" in mi_diccionario)
print("Apellido" in mi_diccionario)

# Inserción

mi_diccionario["Calle"] = "Calle villegas"
print(mi_diccionario)

# Actualización

mi_diccionario["Nombre"] = "austacio"
print(mi_diccionario["Nombre"])

# Eliminación

del mi_diccionario["Calle"]
print(mi_diccionario)

# Otras operaciones

print(mi_diccionario.items())
print(mi_diccionario.keys())
print(mi_diccionario.values())

mi_lista = ["Nombre", 1, "Piso"]

mi_nuevo_diccionario = dict.fromkeys((mi_lista))
print(mi_nuevo_diccionario)
mi_nuevo_diccionario = dict.fromkeys(("Nombre", 1, "Piso"))
print((mi_nuevo_diccionario))
mi_nuevo_diccionario = dict.fromkeys(mi_diccionario)
print((mi_nuevo_diccionario))
mi_nuevo_diccionario = dict.fromkeys(mi_diccionario, "hernan")
print((mi_nuevo_diccionario))

mi_valor = mi_nuevo_diccionario.values()
print(type(mi_valor))

print(mi_nuevo_diccionario.values())
print(list(dict.fromkeys(list(mi_nuevo_diccionario.values())).keys()))
print(tuple(mi_nuevo_diccionario))
print(set(mi_nuevo_diccionario))