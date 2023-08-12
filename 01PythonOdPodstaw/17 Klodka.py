# kłódka jest 5 cyfrowa
# Największa cyfra jest 8 ok
# brak 0 i 6
# suma cyfr wynosiła 21
# cyfry niepowtarzają się
# iloczyn tych cyfr był >= 70 oraz <=400
# ostatnia cyfra jest nieparzysta ok

suma = 0
iloczyn = 1
ilosc = 0
for a in range(1, 9):
    for b in range(1, 9):
        for c in range(1, 9):
            for d in range(1, 9):
                for e in range(1, 9,2):
                    if a+b+c+d+e == 21 and 70 <= a*b*c*d*e <= 400 and (a != 6 and b !=6 and c !=6 and d!=6):
                        if (a!=b and a!=c and a!=d and a!=e and b!=c and b!=d and b!=e and c!=d and c!=e and d!=e):
                            print(a, b, c, d, e)
                            ilosc +=1
print("liczba wariantów ", ilosc)


