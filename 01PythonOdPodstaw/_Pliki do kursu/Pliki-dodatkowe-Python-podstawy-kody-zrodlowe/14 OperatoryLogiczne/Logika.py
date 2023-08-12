value = int(input("Podaj liczbę z przedziału 11-20: "))

# if value > 10:
#     if value <= 20:
#         print("Wartość jest w poprawnym przedziale")
#     else:
#         print("Zła wartość!")
# else:
#     print("Zła wartość!")

# and - "i" / "oraz". Jest operatorem koniunkcji - sprawdza zatem czy dwie wartości są jednocześnie prawdziwe
# or - "lub". Jest operatorem alternatywy - sprawdza zatem czy któraś z dwóch wartości jest prawdziwa
# not - "nie" / "nieprawda, że". Jest operatorem zaprzeczenia - sprawdcza czy zdanie logiczne jest fałszywe

# if value > 10 and value <= 20:
#     print("Wartość jest w poprawnym przedziale")
# else:
#     print("Zła wartość!")

# 10 < x < 15

if (value > 10 and value <= 20) or (value == 35):
    print("Wartość jest w poprawnym przedziale")
else:
    print("Zła wartość!")

# Sprawdzić czy liczba jest z przedziału (0, 100) lub z przedziału [200, 300]