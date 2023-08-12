
for x in range(1, 1000):
    if x != 7 and x!= 77 and x!= 777:
        print(x,  x**2-1000)
print("----")

for x in range(1, 1000):
    if x == 7 and x== 77 and x== 777:
        continue
    print(x,  x**2-1000)



suma = 0
while True:
    napis = input("podaj tekst: ")
    if napis == "wyjdz" or napis == "zakacz" or napis == "exit":
        break
    if len(napis) < 5:
        continue
    suma += len(napis)
    print("suma tekstów powyżej 5 równa", suma)
print("koniec programu")