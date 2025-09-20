
# Trabajo Práctico 3: Estructuras Repetitivas #

# 1.  !

for i in range(1, 101, 1):
    print(i)

# 2.  #

num_int = int(input("Inserte cualquier número entero: "))
i = num_int
digitos = len(str(i))

print(f"Su número tiene {digitos} digitos.")

# 3.  #

num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))

total = 0

if num1 < num2:
    for i in range(num1, num2 + 1):
        if i == num1 or i == num2:
            continue
        total += i
elif num1 > num2:
    for i in range(num2, num1 + 1):
        if i == num1 or i == num2:
            continue
        total += i
else:
    total = 0 

print(f"La suma de estos números da: {total}")

# 4 #

total = 0
numero = int(input("Ingrese un número entero (0 para terminar): "))

while numero != 0:
    total += numero
    numero = int(input("Ingrese otro número (0 para terminar): "))

print("Total acumulado:", total)

# 5. #

import random

n_secreto = [random.randint(0, 9)]
intentos = 0
numero_usuario = None

while numero_usuario != n_secreto:
    numero_usuario = int(input("Adivina el numero (0-9): "))
    intentos += 1

print(f"¡Has acertado! El número era: {n_secreto}. Te has tardado {intentos} intentos.")

