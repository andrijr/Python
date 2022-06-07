# tablica mnożenia
for x in range(1,11):
    for y in range(1,11):
        print("{:2}".format(x * y), end="  ")
    print("")

# napisz program który wyświetli wszystkie możliew kombinację kłódki 4 czyfrowej gdzie:
# pierwsza  liczba jest pażysta
# druga niepażysta
# trzecia podzielna przez 5
# czwarta podzielna przez 3
n =0
for a in range(2, 10,2):
    for b in range(1, 10,2):
        for c in range(5, 10,5):
            for d in range(3, 10,3):
                print(a, b, c, d)
                n += 1

print("")
print("liczba wariantów: ", n)
print("")

# Napisz możliwe kody do kłódki wiadomo jedynie
# kłódka jest 5 cyfrowa
## żadna cyfra nie jest większa niż 6
## nie było w kodzie 0
# 1 3 i 5 cyfra to albo 0 albo 5
# 2 i 4 to niepażyste

for a in range(5, 7, 5):
    for b in range(1, 7, 2):
        for c in range(5, 7, 5):
            for d in range(1, 7, 2):
                for e in range(5, 7, 5):
                    print( a, b, c, d, e)
