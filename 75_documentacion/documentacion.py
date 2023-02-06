class Areas:
  """Esta clase calcula las áreas de diferentes figuras geométricas"""

  def area_cuadrado(lado):
    """Calcula el área de un cuadrado elevando al cuadrado el lado pasado por parámetro"""
    return "El área del cuadrado es: " + str(lado*lado)

  def area_triangulo(base, altura):
    """Calcula el área de un triángulo utilizando los parámetro base y altura"""
    return "El área del triángulo es: " + str((base*altura)/2)

""" print(area_cuadrado(3))
print(area_triangulo.__doc__)
print(area_triangulo(2, 7)) """
help(Areas)