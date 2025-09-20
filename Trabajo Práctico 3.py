
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

# 6. Números pares en descendente #

num = int
for num in range(100, 0, -1):
    print(num)

# 7. Suma de números comprendidos en 0 #

n = int(input("Introduce un entero positivo (>= 0): "))

suma = 0
for i in range(n + 1):
    suma += i

print(f"La suma de 0 a {n} es: {suma}")

# 8. Indicación de pares, impares, negativos y positivos #

numero = 100
pares = impares = negativos = positivos = 0

for i in range(numero):
    n = int(input(f"Ingrese el número {i+1}/{numero}: "))

    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

    if n > 0:
        positivos += 1
    elif n < 0:
        negativos += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Positivos: {positivos}")
print(f"Negativos: {negativos}")

# 9. Cálculo de media de 100 valores #

numero = 100
total = 0

for i in range(numero):
    n = int(input(f"Ingrese el número {i+1}/{numero}: "))
    total += n

media = total / numero
print(f"La media es: {media}")

# 10. Inversión de números #

numero = int(input("Ingresá un entero: "))

signo = -1 if numero < 0 else 1
s = str(abs(numero))
invertido = int(s[::-1])
resultado = signo * invertido

print("Número invertido:", resultado)
