a = int(input("Podaj pierwszą liczbę całkowitą: "))
b = int(input("Podaj drugą liczbę całkowitą: "))

if b > 0 and a > 0:
    x = 1/(a/b) + 1
    suma = 0
    for i in range(int(x)):
        suma += i
    print(suma)