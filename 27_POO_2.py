class Coche():

  # Constructor
  def __init__(self):
    self.__largo_chasis = 250
    self.__ancho_chasis = 120
    self.__ruedas = 4
    self.__en_marcha = False

  def arrancar(self, arrancamos):
    self.en_marcha = arrancamos

    if(self.__en_marcha):
      return 'El coche está en marcha'
    else:
      return 'El coche está parado'

  def estado(self):
    print(f'El coche tiene {self.__ruedas} ruedas. Un ancho de {self.__ancho_chasis} y un largo de {self.__largo_chasis}')

# Instanciar una clase
mi_coche = Coche()
print(mi_coche.arrancar(True))
mi_coche.estado()

print('------- Se crea el segundo objeto --------')

mi_coche2 = Coche()
print(mi_coche2.arrancar(False))
mi_coche2.__ruedas = 2 # no se modifica
mi_coche2.estado()
