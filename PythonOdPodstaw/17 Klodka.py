## kłódka jest 5 cyfrowa
## największą możliwą do wprowadzenia cyfrą jest 8
## brak 0 i 6
# suma cyfr wynosiła 21
# cyfry nie powtarzają się
# iloczyn tych cyfr był >= 70 oraz <= 400
## ostatnia cyfra jest niepażysta

wynik = ""
licznik = 0
for a in range(1, 9):
    #print(a, "a")
    for b in range(1, 9):
        #print(b, "b")
        for c in range(1, 9):
            #print(c, "c")
            for d in range(1, 9):
                #print(d, "d")
                for e in range(1, 9, 2):
                    #print(e, "e")
                    if a != 6 and b != 6 and c != 6 and d != 6 and e != 6:
                        wynik == ""
                        if (a + b + c + d + e) == 21:
                            wynik == ""
                            if a != b and a !=c and a != d and a != e and  b != c and b != d and b != e and c != d and c != e and d != e:
                                wynik == ""
                                if (a * b * c * d * e) >= 70 and (a * b * c * d * e) <= 400:
                                    wynik == ""
                                    licznik += 1
                                    print(a, b, c, d, e)
print("licznik = ", licznik)
