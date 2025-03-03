import copy

x = [1,2,3]
y = list(x)
x.append(4)
print(y)

class MyClass:
    def __init__(self):
        self.a = 0

obiekt = MyClass()
obiekt2 = copy.copy(obiekt)