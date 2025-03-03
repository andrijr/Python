
class Func2:
    def __init__(self, value):
        self.value = value

    def __call__(self, times):
        if type(self.value) == int:
            return self.value * times
        elif type(self.value) == str:
            return self.value.upper() * times
        else:
            return self.value



liczba2 = Func2(3)
print(liczba2(5))

napis2 = Func2("abc")
print(napis2(5))

liczbaZmiennoPrzecinkowa = Func2(2.3)
print(liczbaZmiennoPrzecinkowa(5))