class Foo:
    pole = 3
    def __init__(self):
        self._a = 5
    def get_a(self):
        return self._a
    def set_a(self, value):
        if value < 0:
            self._a = 0
        else:
            self._a = value
    a = property(get_a, set_a)
