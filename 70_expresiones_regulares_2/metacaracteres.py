import re

lista_nombres=[
  "hombres",
  "mujeres",
  "mascotas",
  "camion",
  "camión"
]

for elemento in lista_nombres:
  if re.findall("cami[oó]n", elemento):
    print(elemento)


""" lista_nombres=[
  "hombres",
  "mujeres",
  "mascotas",
  "niños",
  "niñas"
]

for elemento in lista_nombres:
  if re.findall("niñ[oa]s", elemento):
    print(elemento) """

""" lista_nombres=[
  "Ana Gómez",
  "María Martín",
  "Sandra López",
  "Santiago Martín",
  "Sandra Fernandez"
]

for elemento in lista_nombres:
  if re.findall("^Sandra", elemento):
    print(elemento)
  if re.findall("Martín$", elemento):
    print(elemento)
 """

