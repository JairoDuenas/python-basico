import math

def raiz_cuadrada(listaNumeros):
  """
  La fucnión devuelve una lista con la
  raíz cuadrada de los elementos numéricos
  pasados por parámetros en otra lista

  >>> lista=[]
  >>> for i in [4, 9, 16]:
  ...   lista.append(i)
  >>> raiz_cuadrada(lista)
  [2.0, 3.0, 4.0]

  >>> lista=[]
  >>> for i in [4, 9, 16, 50, -78, 90]:
  ...    lista.append(i)
  >>> raiz_cuadrada(lista)
  Traceback (most recent call last):
  ...
  ValueError: math domain error
  """

  return [math.sqrt(n) for n in listaNumeros]

#print(raiz_cuadrada([9, 16, 25, 36]))

import doctest
doctest.testmod()