# Concatenación de operadores de comparación

salario_presidente = int(input('Ingrese salario presidente: '))
print(f'Salario presidente: {salario_presidente}')

salario_director = int(input('Ingrese salario director: '))
print(f'Salario director: {salario_director}')

salario_jefe_area = int(input('Ingrese salario jefe_area: '))
print(f'Salario jefe_area: {salario_jefe_area}')

salario_administrativo = int(input('Ingrese salario administrativo: '))
print(f'Salario administrativo: {salario_administrativo}')

if salario_administrativo < salario_jefe_area < salario_director < salario_presidente:
  print('Todo funciona correctamente')
else:
  print('Hay algún error')
