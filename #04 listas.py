

### Lists ###

# Definición

mi_lista = list()
mi_lista2= []

print(len(mi_lista))

mi_lista = [35, 24, 62, 52, 30, 30, 17]

print(mi_lista)
print(len(mi_lista))

mi_lista2 = [35, 1.77, "hernan", "cordoba"]

print(type(mi_lista))
print(type(mi_lista2))

# Acceso a elementos y búsqueda

print(mi_lista2[0])
print(mi_lista2[1])
print(mi_lista2[-1])
print(mi_lista2[-4])
print(mi_lista.count(30))

print(mi_lista2.index("Argentina"))

edad, altura, nombre, apellido = mi_lista2
print(nombre)

nombre, altura, edad, apellido = mi_lista2[2], mi_lista2[1], mi_lista2[0], mi_lista2[3]
print(edad)

# Concatenación

print(mi_lista + mi_lista2)

# Creación, inserción, actualización y eliminación

mi_lista2.append("hola")# agrega eso a la lista
print(mi_lista2)

mi_lista2.insert(80, "azul") # otra manera de agregar , y tmb agrega numeros
print(mi_lista2)

mi_lista2[1] = "violeta"
print(mi_lista2)

mi_lista2.remove("violeta")
print(mi_lista2)

mi_lista.remove(30)
print(mi_lista)

print(mi_lista.pop())
print(mi_lista)

mi_elemento_pop = mi_lista.pop(2)
print(mi_elemento_pop)
print(mi_lista)

del mi_lista[2]
print(mi_lista)

# Operaciones con listas

mi_nueva_lista = mi_lista.copy()

mi_lista.clear()
print(mi_lista)
print(mi_nueva_lista)

mi_nueva_lista.reverse()
print(mi_nueva_lista)

mi_nueva_lista.sort()
print(mi_nueva_lista)

# Sublistas

print(mi_nueva_lista[1:3])

# Cambio de tipo

mi_lista = "Hola mundo"
print(mi_lista)
print(type(mi_lista))