""" def numero_par(num):
  if num % 2==0:
    return True
"""
""" numeros=[17,24,7,39,8,51,92]
print(list(filter(lambda numero_par: numero_par%2==0, numeros)))
"""
class Empleado:
  def __init__(self, nombre, cargo, salario):
    self.nombre=nombre
    self.cargo=cargo
    self.salario=salario

  def __str__(self):
    return f"{self.nombre} que trabaja como {self.cargo} tiene un salario de ${self.salario}"

lista_empleados=[
  Empleado("Juan", "Director", 750000),
  Empleado("Ana", "Presidenta", 850000),
  Empleado("Antonio", "Administrativo", 25000),
  Empleado("Sara", "Secretaria", 27000),
  Empleado("Mario", "Botones", 21000),
]

salario_altos=filter(lambda empleado:empleado.salario>50000, lista_empleados)
for empleado_salario in salario_altos:
  print(empleado_salario)
