print(3>5)
print(3<5)
print(type(3<5))

x = 5 > 4
y = 5 > 4 or 8 > 7
y = 5 > 4 and 8 > 7

value = int(input("podaj liczbę całkowitą: "))
czyDzielisieNaDwa = value / 2
print(czyDzielisieNaDwa)
czyDzielisieNaDwa = value // 2
print(czyDzielisieNaDwa)
czyDzielisieNaDwa = value % 2
print(czyDzielisieNaDwa)

##
if value % 2 == 0:
    print("podzielna przez 2")
if value % 3 == 0:
    print("podzielna przez 3")
if value % 5 == 0:
    print("podzielna przez 5")

