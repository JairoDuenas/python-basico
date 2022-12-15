mi_tupla = ('Jairo', 13, 1, 1995, 13)
print(mi_tupla[1])
print('Jairo' in mi_tupla)

print(mi_tupla.count(13))
print(len(mi_tupla))

mi_tupla_2 = ('Pedro',) # Tupla unitaria
print(len(mi_tupla_2))

# Tupla sin paréntesis
# mi_tupla_3 = 'Jairo', 13, 1, 1995, 13  empaquetado de una tupla

# desempaquetado de una tupla
mi_tupla_4 = ('Jairo', 13, 1, 1995)
nombre, dia, mes, agno = mi_tupla_4
print(nombre)
print(dia)
print(agno)
print(mes)
