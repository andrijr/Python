# for x in range(1,1001):
#     if x == 7 or x == 77 or x == 777:
#         continue
#     print(x, x**2 - 1000)

# suma = 0
# while True:
#     napis = input("Podaj tekst: ")
#     if napis == "wyjdź" or napis == "zakończ" or napis == "exit":
#         break
#     if len(napis) < 5:
#         continue
#     suma += len(napis)
#     print("Aktualna suma wszystkich wprowadzonych tekstów o długości minimum pięciu znaków to: ", suma)
# print("Koniec programu")

liczba = int(input("Wprowadź liczbę: "))
pierwsza = True
for dzielnik in range(2,liczba):
    if liczba % dzielnik == 0:
        print("Jest to liczba złożona!")
        pierwsza = False
        break

if pierwsza:
    print("Jest to liczba pierwsza!")
