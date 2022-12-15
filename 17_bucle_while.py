""" i = 1
while i <= 10:
  print(f'Ejecución {i}')
  i = i + 1
print('Fin') """

""" edad = int(input('Ingrese su edad: '))

while edad <= 0 or edad > 100:
  print('Ha ingresado una edad incorrecta. Vuelve a intentarlo')
  edad = int(input('Ingrese su edad: '))

print(f'Edad del aspirante es: {edad}') """

import math

print('Progama para calcular la raiz cuadrada de un número')
numero = int(input('Ingrese un número: '))

intentos = 0

while numero < 0:
  print('No se puede hallar la raíz de un número negativo')

  if intentos == 2:
    print('Has ingresado muchos números negativos, El programa ha finalizado')
    break

  numero = int(input('Ingrese un número: '))
  if numero < 0:
    intentos = intentos + 1

if intentos < 2:
  solucion = math.sqrt(numero)
  print(f'La raíz cuadrada de {numero} es {solucion}')

