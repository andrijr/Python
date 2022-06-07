# for i in range(1,101):
#     if i % 17 == 0:
#         if i % 2 == 0:
#             print("liczba", i, "jest podzielna zarówno przez 17 jak i przez 2")
#         print("liczba", i, "jest podzielna tylko przez 17")

# for wiersz in range(1,11):
#     for kolumna in range(1,11):
#         if wiersz * kolumna < 100:
#             print(" ", end="")
#         if wiersz * kolumna < 10:
#             print(" ", end="")
#         print(" " + str(wiersz*kolumna), end="")
#     print("")

for wiersz in range(1,11):
    for kolumna in range(1,11):
        print(" {:3}".format(kolumna * wiersz), end="")
    print("")