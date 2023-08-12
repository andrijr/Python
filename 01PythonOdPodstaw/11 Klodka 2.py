# klódka jest 5 cyfrowa
# żadna cyfra nie jest większa niż 6
# nie było w kodzie 0
# 1 3 5 cyfra to albo 0 albo 5
# druga i 4 były nieparzyste

licznik = 0
for a in range(5, 7,5):
    for b in range(1, 7, 2):
        for c in range(5, 7,5):
            for d in range(1, 7, 2):
                for e in range(5, 7,5):
                    licznik += 1
                    print(a, b, c, d, e)
print("kłódka ma ", licznik, " rozwiązań")