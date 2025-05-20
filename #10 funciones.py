

### Functions ###

# Definición

def mi_funcion():
    print("Esto es una función")


mi_funcion()
mi_funcion()
mi_funcion()

# Función con parámetros de entrada/argumentos


def suma_dos_valores(primer_valor: int, segundo_valor):
    print(primer_valor + segundo_valor)


suma_dos_valores(5, 7)
suma_dos_valores(54754, 71231)
suma_dos_valores("5", "7")
suma_dos_valores(1.4, 5.2)

# Función con parámetros de entrada/argumentos y retorno


def suma_dos_valores_con_retorno(primer_Valor, segundo_valor):
    mi_suma = primer_Valor + segundo_valor
    return mi_suma


mi_resultado = suma_dos_valores(1.4, 5.2)
print(mi_resultado)

mi_resultado = suma_dos_valores_con_retorno(10, 5)
print(mi_resultado)

# Función con parámetros de entrada/argumentos por clave


def print_nombre(nombre, apellido):
    print(f"{nombre} {apellido}")


print_nombre(apellido="Hernan", nombre="Cordoba")

# Función con parámetros de entrada/argumentos por defecto


def print_name_with_default(nombre, apellido, alias="Sin alias"):
    print(f"{nombre} {apellido} {alias}")


print_name_with_default("Cordoba", "Hernan")
print_name_with_default("Cordoba", "Hernan", "MoureDev")

# Función con parámetros de entrada/argumentos arbitrarios


def print_upper_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())


print_upper_texts("Hola", "Python", "MoureDev")
print_upper_texts("Hola")