""" def area_triangulo(base, altura):
  return (base * altura)/2

triangulo1=area_triangulo(5, 7)
triangulo2=area_triangulo(9, 6)

print(triangulo1)
print(triangulo2) """

# Función lambda
"""
area_triangulo=lambda base, altura: (base*altura)/2
triangulo1=area_triangulo(7, 5)
triangulo2=area_triangulo(9, 6)

print(triangulo1)
print(triangulo2) """

""" al_cubo=lambda numero:pow(numero, 3)

#al_cubo=lambda numero:numero**3
print(al_cubo(5)) """

# destacar_valor=lambda comision:"¡{}! $".format(comision)
destacar_valor=lambda comision:f"¡{comision}! $"

comison_ana=15585

print(destacar_valor(comison_ana))


