from televisores.marca import Marca

class TV:
    numTV = 0

    def __init__(self, marca: Marca, estado: bool):
        self.canal = 1
        self.volumen = 1
        self.precio = 500
        self.estado = estado
        self.marca = marca
        self.control = None  # El control será enlazado después
        TV.numTV += 1

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def setCanal(self, canal: int):
        if 0 < canal < 120 and self.estado:
            self.canal = canal

    def getCanal(self):
        return self.canal

    def setPrecio(self, precio: int):
        self.precio = precio

    def getPrecio(self):
        return self.precio

    def setVolumen(self, volumen: int):
        if 0 <= volumen <= 7 and self.estado:
            self.volumen = volumen

    def getVolumen(self):
        return self.volumen

    def setControl(self, control):
        self.control = control

    def getControl(self):
        return self.control

    @classmethod
    def getNumTV(cls):
        return cls.numTV

    def turnOff(self):
        self.estado = False

    def turnOn(self):
        self.estado = True

    def getEstado(self):
        return self.estado

    def canalUp(self):
        if self.canal < 120 and self.estado:
            self.canal += 1

    def canalDown(self):
        if self.canal > 1 and self.estado:
            self.canal -= 1

    def volumenUp(self):
        if self.volumen < 7 and self.estado:
            self.volumen += 1

    def volumenDown(self):
        if self.volumen > 0 and self.estado:
            self.volumen -= 1