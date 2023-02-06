def area_triangulo(base, altura):
  """
  Calcula el área de un triángulo dado

  >>> area_triangulo(3, 6)
  'El área del triángulo es: 9.0'

  >>> area_triangulo(4, 5)
  'El área del triángulo es: 10.0'

  >>> area_triangulo(9, 3)
  'El área del triángulo es: 13.5'
  """
  return "El área del triángulo es: " + str((base*altura)/2)

import doctest
doctest.testmod()