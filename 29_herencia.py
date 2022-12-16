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

class Furgoneta(Vehiculos):
    def carga(self, cargar):
        self.cargado = cargar

        if(self.cargado):
            return 'La furgoneta está cargada'
        else:
            return 'La furgoneta o está cargada'

class Moto(Vehiculos):
    hace_caballito = ''
    def caballito(self):
        self.hace_caballito = 'Voy haciendo caballito'

    def estado(self):
        print(f'Marca: {self.marca} \nModelo: {self.modelo} \nEn marcha: {self.en_marcha} \nAcelerando: {self.acelera} \nFrenado: {self.frena} \n{self.hace_caballito}')

class V_electrico():
    def __init__(self):
        self.autonimia = 100
    def cargar_energia(self):
        self.cargando = True

mi_moto = Moto('Honda', 'CBR')
mi_moto.caballito()
mi_moto.estado()

mi_furgoneta = Furgoneta('Renault', 'Kangoo')
mi_furgoneta.arrancar()
mi_furgoneta.estado()
print(mi_furgoneta.carga(True))


class Bici_electrica(V_electrico, Vehiculos):
    pass

mi_bici = Bici_electrica()