

### Variables ###

mi_variable= "variable 1"
print(mi_variable)

mi_variable2 = 5
print(mi_variable2)

mi_variable_int_a_str = str(mi_variable2)
print(mi_variable2)
print(type(mi_variable_int_a_str))

mi_variable_boolanea = False
print(mi_variable_boolanea)

# Concatenación de variables en un print
print(mi_variable, mi_variable_int_a_str, mi_variable_boolanea)
print("Este es el valor de:", mi_variable_boolanea)

# Algunas funciones del sistema
print(len(mi_variable))

# Variables en una sola línea. ¡Cuidado con abusar de esta sintaxis!
nombre, apellido, alias, edad = "Hernán", "Córdoba", 'No tengo apodo', 17
print("Me llamo:", nombre, apellido, ". Mi edad es:",
      edad, ". Y mi apodo es:", alias)

# Inputs
nombre1 = input('¿Cuál es tu nombre? ')
edad1 = input('¿Cuántos años tienes? ')
print(nombre1)
print(edad1)

# Cambiamos su tipo
nombre = 35
edad = "Hernan"
print(nombre)
print(edad)

# ¿Forzamos el tipo?
address: str = "Mi dirección"
address = True
address = 7
address = 1.6
print(type(address))