mi_variable= "variable 1"
print(mi_variable)

mi_variable2 = 5
print(mi_variable2)

mi_variable_int_a_str = str(mi_variable2)
print(mi_variable2)
print(type(mi_variable_int_a_str))

mi_variable_boolanea = False
print(mi_variable_boolanea)


print(mi_variable, mi_variable_int_a_str, mi_variable_boolanea)
print("Este es el valor de:", mi_variable_boolanea)


print(len(mi_variable))


nombre, apellido, alias, edad = "Hernán", "Córdoba", 'No tengo apodo', 17
print("Me llamo:", nombre, apellido, ". Mi edad es:",
      edad, ". Y mi apodo es:", alias)


nombre1 = input('¿Cuál es tu nombre? ')
edad1 = input('¿Cuántos años tienes? ')
print(nombre1)
print(edad1)


nombre = 35
edad = "Hernan"
print(nombre)
print(edad)

address: str = "Mi dirección"
address = True
address = 7
address = 1.6
print(type(address))
