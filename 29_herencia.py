class Vehiculos():

  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo
    self.en_marcha = False
    self.acelera = False
    self.frena = False

  def arrancar(self):
    self.en_marcha = True

  def acelerar(self):
    self.acelera = True

  def frenar(self):
    self.frena = True

  def estado(self):
    print(f'Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.en_marcha} \nAcelerando: {self.acelera} \nFrenado: {self.frena}')

class Moto(Vehiculos):
  pass

mi_moto = Moto('Honda', 'CBR')
mi_moto.estado()

