x = "zmienna przechowuje tekst"
# "0123456..."
y = x[3]
z = x[0] + x[1] + " tekst " + x[3:6]
a = 3
b = 6
c = a + b
d = "3"
e = "6"
f = d + e



print(type(x))
print(x[1])
print(y)
print(z)
print(c)
print(f)
print(x.upper())
print(len(x))

tekstZKreska = x[0:8] + "- " + x[8:18]
print(tekstZKreska)