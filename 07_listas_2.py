mi_lista = ['Jairo', 5, True, 78.35]

print(mi_lista[:])
print(mi_lista[2])
print(mi_lista[-2])
print(mi_lista[-3])
#print(mi_lista[7]) IndexError: list index out of range

print(mi_lista[0:3])
print(mi_lista[:3])
print(mi_lista[1:3])
print(mi_lista[2:])

mi_lista.append('Sandra')
print(mi_lista[:])

mi_lista.insert(2, 'Samuel')
print(mi_lista[:])

mi_lista.extend(['Pedro', 'Carlos', 'María'])
print(mi_lista)
print(mi_lista.index('Jairo'))
print('Martha' in mi_lista)

mi_lista.remove('Carlos')
print(mi_lista[:])
mi_lista.remove(5)
print(mi_lista[:])

mi_lista.pop()
print(mi_lista[:])

mi_lista2 = ['Luis', 4, 25]
mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)

mi_lista4 = ['Sandra', 7, True, 65.35] * 3
print(mi_lista4[:])
