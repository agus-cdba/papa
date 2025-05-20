
### Operadores Aritméticos ###

# Operaciones con enteros
print(2 + 4) #suma
print(5 - 4) #resta 
print(8 * 4) #multiplicacion
print(24 / 4) #division
print(10 % 3) #da el resto de la division
print(10 // 3) #da el cociente
print(2 ** 3) #potencia
print(2 ** 3 + 3 - 7 / 1 // 4)#combinacion

# Operaciones con cadenas de texto
print("Hola " + "mundo " + "como va?")
print("Hola " + str(5))

# Operaciones mixtas
print("andate riquelme " * 5)
print("andate riquelme " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores Comparativos ###

# Operaciones con enteros
print(3 > 4) #mayor que 
print(3 < 4) #menor que 
print(3 >= 4) #mayor o igual que
print(4 <= 4) #menos o igual que
print(3 == 4) #igual que
print(3 != 4) #ya no se que es eso 


# Operaciones con cadenas de texto
print("Hola" > "chauu")
print("Hola" < "chauu")
print("aaaaaaa" >= "aaaaab")  # Ordenación alfabética por ASCII
print(len("aaaaa") >= len("abaa"))  # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### Operadores Lógicos ###

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))
print(not (3 > 4))