# Kłódka jest pięciocyfrowa ABCDE
# Największą możliwą do wprowadzenia cyfrą jest 8
# Brak 0 i 6
# Suma cyfr wynosiła 21
# Cyfry nie powtarzają się
# Iloczyn cyfr był większy bądź równy 70 i mniejszy bądź równy 400
# Ostatnia cyfra jest nieparzysta

# licznik = 0
# for a in range(1,9):
#     for b in range(1,9):
#         for c in range(1,9):
#             for d in range(1,9):
#                 for e in range(1,9):
#                     if a != 6 and b != 6 and c !=6 and d != 6 and e != 6:
#                         if a + b + c + d +e == 21 and 400 >= a * b * c * d * e >= 70:
#                             if a != b and a != c and a != d and a != e and b != c and b != d and b != e and c != d and c != e and d != e:
#                                 if e % 2 == 1:
#                                     licznik += 1
#                                     print(str(a)+str(b)+str(c)+str(d)+str(e))
# print("Ilość możliwości to:", licznik)

# Kłódka jest pięciocyfrowa
# Liczba przedstawiająca kłódkę była liczbą pierwszą
# Suma cyfr była z zakresu 30 i 40
# Nie było żadnego 0