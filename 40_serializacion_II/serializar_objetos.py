import pickle

class Vehiculo():

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

coche1 = Vehiculo('Mazda', 'MX5')
coche2 = Vehiculo('Seat', 'Leon')
coche3 = Vehiculo('Renault', 'Megane')

coches = [coche1, coche2, coche3]
fichero =  open('los_coches', 'wb')

pickle.dump(coches, fichero)
fichero.close()
del (fichero)

# Recuperando fichero
fichero_apertura = open('los_coches', 'rb')
mis_coches = pickle.load(fichero_apertura)
fichero_apertura.close()

for c in mis_coches:
    print(c.estado())