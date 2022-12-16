class Coche():
  def desplazamiento(self):
    print('Me desplazo utilizando cuatro ruedas')

class Moto():
  def desplazamiento(self):
    print('Me desplazo utilizando dos ruedas')

class Camion():
  def desplazamiento(self):
    print('Me desplazo utilizando seis ruedas')

def desplazamiento_vehiculo(vehiculo):
  vehiculo.desplazamiento()

mi_vehiculo = Moto()
desplazamiento_vehiculo(mi_vehiculo)

mi_vehiculo2 = Coche()
desplazamiento_vehiculo(mi_vehiculo2)