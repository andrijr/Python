class Foo:
    pole = 3
    def __init__(self):
        self._a = 5
    @property
    def a(self):
        return self._a
    @a.setter
    def a(self, value):
        if value < 0:
            self._a = 0
        else:
            self._a = value

