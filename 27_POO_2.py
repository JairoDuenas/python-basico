class Coche():

  # Constructor
  def __init__(self):
    self.__largo_chasis = 250
    self.__ancho_chasis = 120
    self.__ruedas = 4
    self.__en_marcha = False

  def arrancar(self, arrancamos):
    self.__en_marcha = arrancamos

    if(self.__en_marcha):
      chequeo = self.__chequeo_interno()

    if(self.__en_marcha and chequeo):
      return 'El coche está en marcha'

    elif(self.__en_marcha and chequeo==False):
      return 'Algo ha salido mal en el chequeo. No se puede arrancar'
    else:
      return 'El coche está parado'

  def estado(self):
    print(f'El coche tiene {self.__ruedas} ruedas. Un ancho de {self.__ancho_chasis} y un largo de {self.__largo_chasis}')

# encapsulado del método (__chequeo_interno())
  def __chequeo_interno(self):
    print('Realizando chequeo interno')

    self.gasolina = 'ok'
    self.aceite = 'ok'
    self.puertas = 'cerradas'

    if(self.gasolina == 'ok' and self.aceite == 'ok' and self.puertas == 'cerradas'):
      return True
    else:
      return False

# Instanciar una clase
mi_coche = Coche()
print(mi_coche.arrancar(True))
mi_coche.estado()

print('------- Se crea el segundo objeto --------')

mi_coche2 = Coche()
print(mi_coche2.arrancar(False))
mi_coche2.estado()
