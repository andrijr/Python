# wyświetl wyszystkie kombinacje 4 cyfrowej kłódki gdzie
# pierwsza cyfra jest parzysta
# druga nieparzysta
# trzecia podzielna przez 5
# czwarta podzielna przez 3

licznik = 0
for a in range(2,10, 2):
    for b in range(1,10,2):
        for c in range(5,10, 5):
            for d in range(3,10, 3):
                licznik +=1
                print(a, "", b, "", c, "", d, "")
print("kłódka ma ", licznik, " rozwiązań")
