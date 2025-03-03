# wyrażenia listowe
# [wyrażenie for element in kolekcja if warunek]

parzyste = [x for x in range(11) if x%2==0]
print(parzyste)

parzyste = [x*x for x in range(11) if x%2==0]
print(parzyste)

parzyste2 = []
for x in range(11):
    if x*x % 2 == 0:
        parzyste2.append(x*x)
print(parzyste2)

napis = "Jakiś jeden tekst 234 tutaj jeden jest 5 5"
lista = [int(znak) for znak in napis if znak.isdigit()]
print(lista, type(lista))

zbior = {int(znak) for znak in napis if znak.isdigit()}
print(zbior, type(zbior))

