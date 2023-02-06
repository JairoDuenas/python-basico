def comprueba_email(mailUsuario):
  """
  La función comprueba email evalúa un email
  recibiendo en busca de la @. Si tiene una @
  es correcto, si tiene más de una @ es incorrecto
  si la @ está al final es incorrecto.

  >>> comprueba_email('jairo@cursos.es')
  True

  >>> comprueba_email('jairocursos.es@')
  False

  >>> comprueba_email('jairocursos.es')
  False

  >>> comprueba_email('jairo@cursos@.es')
  False
  """

  arroba=mailUsuario.count('@')

  if (arroba!=1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0):
    return False
  else:
    return True

import doctest
doctest.testmod()