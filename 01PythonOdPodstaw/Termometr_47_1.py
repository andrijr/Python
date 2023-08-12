class Termometr:
    def __init__(self, temp = 0):
        self.celsjusz = temp

    def setTemperature(self, temp, unit = 'C'):
        if unit == 'C':
            self.celsjusz = temp
        elif unit == 'K':
            self.celsjusz = temp + 273.15
        else:
            self.celsjusz = (temp - 32) * (5/9)

    def getTemperature(self, unit = 'C'):
        if unit == 'C':
            return self.celsjusz
        elif unit == 'K':
            return  self.celsjusz - 273.15
        else:
            return ((self.celsjusz * (5 / 9) ) + 32)
