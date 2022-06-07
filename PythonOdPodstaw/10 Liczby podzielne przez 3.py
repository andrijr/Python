# oblicz sume liczb od 1 do 1000 podzielnych przez 3 oraz sumę liczb niepodzielnych przez 3

n = int(input("Podaj liczbę graniczną: "))
a = int(input("Podaj przez jaką liczbę mają być podzielne liczby: "))
suma1 = 0.0
suma2 = 0.0

for x in range(0, n+1, a):
    # print(x)
    suma1 += x

for y in range(0, n+1):
    # print(y)
    suma2 += y
suma2 = suma2 - suma1
print("suma liczb podzielnych przez ", a, "=", suma1)
print("suma liczb niepodzielnych przez ", a, "=", suma2)



suma1 = 0.0
suma2 = 0.0
for z in range(0, n+1):
    # print(z)
    t = z % a
    if t == 0:
        suma1 += z
    else:
        suma2 += z
print("suma liczb podzielnych przez ", a, "=", suma1)
print("suma liczb niepodzielnych przez ", a, "=", suma2)