class Tetragon:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = d
        self.d = d

    def perimetr(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        pass

class Rectagle(Tetragon):
    def __init__(self, a, b):
        Tetragon.__init__(self, a, b, a, b)

    def area(self):
        return self.a * self.b

class Square(Rectagle):
    def __init__(self, a):
        Rectagle.__init__(self, a, a)



