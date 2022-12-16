class Coche():
  largo_chasis = 250
  ancho_chasis = 120
  ruedas = 4
  en_marcha = False

  def arrancar(self):
    self.en_marcha = True

  def estado(self):
    if(self.en_marcha):
      return 'El coche está en marcha'
    else:
      return 'El coche está parado'

# Instanciar una clase
mi_coche = Coche()

print(f'El largo del coche es: {mi_coche.largo_chasis}')
print(f'El coche tiene {mi_coche.ruedas} ruedas ')

mi_coche.arrancar()

print(mi_coche.estado())