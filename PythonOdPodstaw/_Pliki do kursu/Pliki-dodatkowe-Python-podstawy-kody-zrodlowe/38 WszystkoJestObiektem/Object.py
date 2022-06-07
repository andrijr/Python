def dodaj(a,b):
    return a + b

def pomnoz(a,b):
    return a * b

def podziel(a,b):
    return a / b

def odejmij(a,b):
    return a - b

def podzielCalkowicie(a,b):
    return a // b

def podajReszte(a,b):
    return a % b

# tupla = (1,2)
# lista = [2, "4s", 3.3, tupla, dodaj]
# print(lista)

print("Program wykonuje na raz podstawowe działania arytmetyczne")

listaFunkcji = [dodaj, odejmij, pomnoz, podziel, podzielCalkowicie, podajReszte]
listaOpisow = ["dodawania", "odejmowania", "mnozenia", "dzielenia", "dzielenia całkowitego", "dzielenia z resztą"]

x = float(input("Podaj pierwszą liczbę: "))
y = float(input("Podaj drugą liczbę: "))

for i in range(0,len(listaFunkcji)):
    print("Wynik", listaOpisow[i], "wynosi:", listaFunkcji[i](x,y))

for funkcja in listaFunkcji:
    print(funkcja(x,y))