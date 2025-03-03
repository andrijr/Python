

i = 1
if i == 3:
    print(True)
else:
    print(False)


i = 2
while i >4:
    i -= 1
    print("Instrukcja w pętli while")
else:
    print("Instrukcja else")

print("Instrukcja za pętlą while")



i = 10
while i >4:
    i -= 1
    print("Instrukcja w pętli while")
else: # kiedy warunek przestaje byc prawdziwy wchodzi w instrukcje else
    print("Instrukcja else")

print("Instrukcja za pętlą while")

print("---")
i = 10
while i >4:
    i -= 1
    print("Instrukcja w pętli while")
    if i == 7:
        break # break w tym miejscu powoduję że else się nie wykona
else: # kiedy warunek przestaje byc prawdziwy wchodzi w instrukcje else
    print("Instrukcja else")
print("Instrukcja za pętlą while")

print("--- zgadnij liczbę ---")
import random

zgadywana = random.randint(1,1000)
odpowiedz = int(input("podaj liczbę do odgadnięcia lub z poza przedziału 1-1000 żew wyjśc z gry " ))
while 1<=odpowiedz<=1000:
    if odpowiedz>zgadywana:
        print("Zgadywana liczba jest mniejszza")
    elif odpowiedz<zgadywana:
        print("Zgadywan liczba jest większa")
    else:
        print("Liczba odgadnięta i jest =", zgadywana)
        break
    odpowiedz = int(input("Podaj inną liczbę"))
else:
    print("wyjście z gry przed odgadnięciem, wylosowaną liczbą była: ", zgadywana)
print("Dziękuję")

for i in range(10):
    print(i)
    if i % 5 ==0 and i != 0:
        break
else:
    print("wyszedleś z pętli")
print("Dalsze instrukcje")