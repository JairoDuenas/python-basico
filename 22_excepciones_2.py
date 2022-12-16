""" def suma(num1, num2):
  return num1 + num2

def resta(num1, num2):
  return num1 - num2

def multiplica(num1, num2):
  return num1 * num2

def divide(num1, num2):

  try:
    return num1 / num2
  except ZeroDivisionError:
    print('No se puede dividir entre 0')
    return 'Operación errónea'

while True:
  try:
    op1 = (int(input('Ingrese el primer número: ')))
    op2 = (int(input('Ingrese el segundo número: ')))
    break

  except ValueError:
    print('Los valores ingresados no son correctos. Ingrese un número válido')

operación = input('Ingrese la operación a realizar (suma, resta, multiplica, divide): ')

if operación == 'suma':
  print(suma(op1, op2))

elif operación == 'resta':
  print(resta(op1, op2))

elif operación == 'multiplica':
  print(multiplica(op1, op2))

elif operación == 'divide':
  print(divide(op1, op2))

else:
  print('Operación no completada')

print('Operación ejecutada. Continuación de ejecución del progarama')
 """
def divide():

  try:
    op1 = (float(input('Ingrese el primer número: ')))
    op2 = (float(input('Ingrese el segundo número: ')))

    print(f'La división es: {op1/op2}')

  except ValueError:
    print('El valor ingresado es erróneo')
  except ZeroDivisionError:
    print('No se puede dividir entre 0')

  finally:
    print('Cálculo finalizado')

divide()