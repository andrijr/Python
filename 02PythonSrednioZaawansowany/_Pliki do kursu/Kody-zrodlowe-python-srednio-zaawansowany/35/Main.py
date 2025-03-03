class Obliczenia:
    def silnia(self,n):
        iloczyn = 1
        for i in range(1,n+1):
            iloczyn *= i
        return iloczyn

obiekt = Obliczenia()