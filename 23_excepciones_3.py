import math

def calcula_raiz(num1):

  if num1 < 0:
    raise ValueError('El número no puede ser negativo')

  else:
    return math.sqrt(num1)

op1 = int(input('Ingrese un número: '))

try:
  print(calcula_raiz(op1))
except ValueError as ErrorDeNumeroNegativo:
  print(ErrorDeNumeroNegativo)

print('Terminando programa')
