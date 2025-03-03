
class Func:
    # metoda specjalna uruchamiana przy tworzeniu obiektu
    # def __int__(self):
    def __init__(self, number):
        self.number = number
    # metoda specjalna uruchamiana przy wywolanie funkcji number
    # def __call__(self, *args, **kwargs):
    def __call__(self, times):
        return self.number * times

    # metoda uruchamiana w czasie tworzenia obiektu służy do reprezentacji obiektu
    # def __str__(self):


liczba = Func(3)
print(liczba(5))

napis = Func("abc")
print(napis(5))