from televisores.marca import Marca
from televisores.control import Control

class TV:
    numTV = 0
    def __init__(self, marca: Marca,  estado: bool,  control: Control):
        self.canal = 1
        self.volumen = 1
        self.precio = 500
        self.estado = estado
        self.marca = marca
        self.control = control
        numTV += 1
    
    def setMarca(self, marca):
        self.marca = marca
    
    def getMarca(self):
        return self.marca
    
    def setCanal(self, canal: int):
        if canal > 0 and canal < 120 and self.estado == True:
            self.canal = canal
    
    def getCanal(self):
        return self.canal
    
    def setPrecio(self, precio: int):
        self.precio = precio

    def getPrecio(self):
        return self.precio
    
    def setVolumen(self, volumen: int):
        if volumen >= 0 and volumen <= 7 and self.estado == True:
            self.volumen = volumen

    def getVolumen(self):
        return self.volumen
    
    def setControl(self, control: Control):
        self.control = control

    def getControl(self):
        return self.control
    
    def getNumTV(self):
        return self.numTV
    
    def turnOff(self):
        self.estado = False

    def turnOn(self):
        self.estado = True

    def getEstado(self):
        return self.estado
    
    def canalUp(self):
        if self.canal < 120 and self.estado == True:
            self.canal += 1
    
    def canalDown(self):
        if self.canal > 1 and self.estado == True:
            self.canal -= 1

    def volumenUp(self):
        if self.volumen <7 and self.estado == True:
            self.volumen += 1
    
    def volumemDown(self):
        if self.volumen > 0 and self.estado == True:
            self.volumen -= 1
    
    