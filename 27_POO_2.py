class Coche():

  # Constructor
  def __init__(self):
    self.largo_chasis = 250
    self.ancho_chasis = 120
    self.ruedas = 4
    self.en_marcha = False

  def arrancar(self, arrancamos):
    self.en_marcha = arrancamos

    if(self.en_marcha):
      return 'El coche está en marcha'
    else:
      return 'El coche está parado'

  def estado(self):
    print(f'El coche tiene {self.ruedas} ruedas. Un ancho de {self.ancho_chasis} y un largo de {self.largo_chasis}')

# Instanciar una clase
mi_coche = Coche()
print(mi_coche.arrancar(True))
mi_coche.estado()

print('------- Se crea el segundo objeto --------')

mi_coche2 = Coche()
print(mi_coche2.arrancar(False))
mi_coche2.estado()
