### Sets ###

# Definición

mi_set = set()
mi_otro_set = {}

print(type(mi_set))
print(type(mi_otro_set))  # Inicialmente es un diccionario

mi_otro_set = {"hola", "chau", 18}
print(type(mi_otro_set))

print(len(mi_otro_set))

# Inserción

mi_otro_set.add("hola q hace")

print(mi_otro_set)  # Un set no es una estructura ordenada

mi_otro_set.add("hola q hace")  # Un set no admite repetidos

print(mi_otro_set)

# Búsqueda

print("agustin" in mi_otro_set)
print("agusto" in mi_otro_set)

# Eliminación

mi_otro_set.remove("agustin")
print(mi_otro_set)

mi_otro_set.clear()
print(len(mi_otro_set))

del mi_otro_set
# print(mi_otro_set) NameError: name 'mi_otro_set' is not defined

# Transformación

mi_set = {"hernan", "cordoba", 35}
mi_lista = list(mi_set)
print(mi_lista)
print(mi_lista[0])

mi_otro_set = {"paty", "carne", "pollo"}

# Otras operaciones

my_new_set = mi_set.union(mi_otro_set)
print(my_new_set.union(my_new_set).union(mi_set).union({"milanesa con papas fritas", "C#"}))
print(my_new_set.difference(mi_set))