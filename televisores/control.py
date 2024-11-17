class Control:
    def __init__(self):
        self.tv = None

    def getTv(self):
        return self.tv

    def setTv(self, tv):
        self.tv = tv

    def turnOn(self):
        self.tv.turnOn()

    def turnOff(self):
        self.tv.turnOff()

    def canalUp(self):
        self.tv.canalUp()

    def canalDown(self):
        self.tv.canalDown()

    def volumenUp(self):
        self.tv.volumenUp()

    def volumenDown(self):
        self.tv.volumenDown()

    def setCanal(self, dato):
        self.tv.setCanal(dato)

    def setVolumen(self, volumen):
        self.tv.setVolumen(volumen)

    def enlazar(self, tv):
        from televisores.tv import TV  
        if isinstance(tv, TV):
            self.tv = tv
            tv.setControl(self)