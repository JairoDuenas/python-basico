class Empleado:
  def __init__(self, nombre, cargo, salario):
    self.nombre=nombre
    self.cargo=cargo
    self.salario=salario

  def __str__(self):
    return f"{self.nombre} que trabaja como {self.cargo} tiene un salario de ${self.salario}"

lista_empleados=[
  Empleado("Juan", "Director", 6700),
  Empleado("Ana", "Presidenta", 7500),
  Empleado("Antonio", "Administrativo", 2100),
  Empleado("Sara", "Secretaria", 2150),
  Empleado("Mario", "Botones", 1800),
]

def calculo_comision(empleado):
  if (empleado.salario<=3000):
    empleado.salario=empleado.salario*1.03
  return empleado

lista_empleados_comision=map(calculo_comision, lista_empleados)

for empleado in lista_empleados_comision:
  print(empleado)
