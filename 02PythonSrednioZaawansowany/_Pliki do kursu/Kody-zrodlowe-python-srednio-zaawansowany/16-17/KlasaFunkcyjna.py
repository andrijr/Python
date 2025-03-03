class Func:
    def __init__(self,value):
        self.value = value

    def __call__(self, times):
        if type(self.value) == int:
            return self.value * times
        elif type(self.value) == str:
            return self.value.upper() * times
        else:
            return self.value

liczba = Func(3)
print(liczba(5))

napis = Func("abc")
print(napis(5))

liczbaZmiennoprzecinkowa = Func(3.3)
print(liczbaZmiennoprzecinkowa(5))