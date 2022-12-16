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
    hace_caballito = ''
    def caballito(self):
        self.hace_caballito = 'Voy haciendo caballito'

    def estado(self):
        print(f'Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.en_marcha} \nAcelerando: {self.acelera} \nFrenado: {self.frena} \n{self.hace_caballito}')


mi_moto = Moto('Honda', 'CBR')
mi_moto.caballito()
mi_moto.estado()
