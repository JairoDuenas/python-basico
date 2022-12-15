def generar_pares(limite):
  num = 1
  mi_lista = []

  while num < limite:
    mi_lista.append(num * 2)
    num += 1
  return mi_lista

print(generar_pares(10))

# -------------------------------#

def genera_pares2(limite):
  num = 1
  while num < limite:
    yield num * 2
    num += 1
devuelve_pares2 = genera_pares2(10)

print(next(devuelve_pares2))
print('Más código')

print(next(devuelve_pares2))
print('Más código')

print(next(devuelve_pares2))

""" for i in devuelve_pares2:
  print(i) """