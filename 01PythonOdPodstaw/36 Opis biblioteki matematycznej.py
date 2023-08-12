

import math
from math import sin

from math import *

print(round(4.5))
print(round(4.6))
print(math.floor(4.6))
print(math.ceil(4.5))
# sum lepiej urzywać do liczb całkowitychh
print(sum([1,2,3,4,5,6,7,8,9,10]))

# fsum lepiej urzywać do liczb zmiennoprzecinkowych
print(sum([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,]))
print(math.fsum([0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1,]))

# największy wspólny dzielnik
print(math.gcd(8,4)) # 4

# pierwiastek kwadratowy
print(math.sqrt(9))

# potęga
print(math.pow(3,2))
# pierwiastek na podstawie potęgi
print(math.pow(9,1/2))

# logarytm 2 do jakiej potęgi należy podnieść 2 aby wyszła wskazana liczba
print(math.log2(64))
print(math.log(64,2))

# logarytm 10 do jakiej potęgi należy podnieść 10 aby wyszła wskazana liczba
print(math.log10(100))
print(math.log(100,10))

# logarytm  e do jakiej potęgi należy podnieść e aby wysła wskazana liczba
print(math.log(100))

# logarytm dowolny
print(math.log(9,3))

# funkcje trygonometryczne
print(math.sin(0))
print(math.cos(0))

# funkcja operuję na radianach
print(math.sin(30)) # 30 radianów
print(math.sin(math.radians(30))) # 30 stopni

print(math.pi)
print(math.e)