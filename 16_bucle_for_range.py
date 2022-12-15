""" for i in range(5, 51, 5):
  print(f'Valor de la variable {i}') """

valido = False
email = input('Ingrese el email: ')
for i in range(len(email)):
  if email[i] == '@':
    valido = True

if valido:
  print('Email correcto')
else:
  print('Email incorrecto')