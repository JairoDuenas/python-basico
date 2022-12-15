# Condicionales con operadores lógicos #

""" print('Programa de becas año 2022')

distancia_escuela = int(input('Ingrese distancia a la escuela en km: '))
print(f'Distancia: {distancia_escuela} km')

numero_hermanos = int(input('Ingrese el número de hermanos: '))
print(f'Hermanos: {numero_hermanos}')

salario_familiar = int(input('Ingrese el salario familiar anual: '))
print(f'Salario familiar anual: {salario_familiar}')

if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 20000:
  print('Tienes derecho a beca')
else:
  print('No tienes derecho a beca') """

# Ejercicio operador in #
print('Asignaturas optativas año 2022')
print('Asignaturas optativas: Informática gráfica - Pruebas de software - Usabilidad y accesibilidad')
opcion = input('Escribe la asignatura escogida: ')

asignatura = opcion.lower()

if asignatura in ('informática gráfica', 'pruebas de software', 'usabilidad y accesibilidad'):
  print(f'Asignatura elegida: {asignatura.capitalize()}')
else:
  print('La asignatura escogida no está contemplada')