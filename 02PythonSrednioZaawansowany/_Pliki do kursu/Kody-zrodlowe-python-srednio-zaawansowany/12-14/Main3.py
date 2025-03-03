#lista = [wyrażenie for element in kolekcja if warunek]

parzyste = [x*x for x in range(11) if x % 2 == 0]
print(parzyste)

squares = []
for i in range(11):
    if i % 2 == 0:
        squares.append(i*i)
print(squares)

napis = "Jakiś 1tekst2 34 tutaj1 jest5"
lista = {int(znak) for znak in napis if znak.isdigit()}
print(lista)