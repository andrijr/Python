# zamiana zmiennych to jest coś co się wykonuje bardzo często

import copy

a = 3
b = 5

print("1 sposób najbardziej popularny ale nie polecany")
temp = a
a = b
b = temp
print('a =', a, 'b = ', b)

a = 3
b = 5

print("2 sposób też nie jest zalecany")
b = a + b
a = b - a
b = b - a
print('a =', a, 'b = ', b)

a = 3
b = 5

print("3 sposób polecany metoda swapowania")
a, b = b, a
c, d, e, = [1,2,3]
x, y = 7, 8
print('a =', a, 'b = ', b)
print(a, b, c,d,e,x,y)

x = True
y = False
a = 1
print(x==1)
print(type(x))

# w słowniku nadpisuję się zostaje tylko c
slownik = {True: 'a', 1: 'b', 1.0: 'c'}
print(slownik)
print(slownik[True])

print(True==1)
print(True==1.0)

x = [1,2,3]
y = x
x.append(4)
print(y)

x = [1,2,3]
y = []
for element in x:
    y.append(element)
x.append(5)
print(x,y)

# kopiowanie do nowego obiektu a nie do tego samego obiektu o innej nazwie
x = [1,2,3]
y = []
y = list(x)
x.append(6)
print(x,y)

class MyClass:
    def __init__(self):
        self.a = 0

# przypisanie dwóch wskaźników do tej samej zmiennej
obiekt = MyClass()
obiekt2 = obiekt

# skopiowanie do nowego obiektu
obiekt3 = MyClass()
obiekt4 = copy.copy(obiekt3)


