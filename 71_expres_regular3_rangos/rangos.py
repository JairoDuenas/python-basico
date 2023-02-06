import re

lista_nombres=[
  'Ana',
  'Pedro',
  'María',
  'Rosa',
  'Sandra',
  'Celia'
]

for elemento in lista_nombres:
  if re.findall('[o-t]$', elemento):
    print(elemento)
# -----------------------------------------
lista_nombres2=[
  'Ma.1',
  'Se1',
  'Ma2',
  'Ba1',
  'Ma:3',
  'Va1',
  'Va2',
  'Ma4',
  'MaA',
  'Ma.5',
  'MaB',
  'Ma:C'
]

for elemento2 in lista_nombres2:
  #if re.findall('Ma[0-3]', elemento2):
  #if re.findall('Ma[^0-3]', elemento2):
  #if re.findall('Ma[0-3A-B]', elemento2):
  if re.findall('Ma[.:]', elemento2):
    print(elemento2)