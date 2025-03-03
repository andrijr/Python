# żeby można było urzyć mniejszej ilości zmiennych powinne być dodane parametry domyślne
# parametry domyślne powinne być ostatnimi parametrami funkcji
# możemy napisać jakiego typu powinne być parametry

# dodajemy parametr domyślny
def dodaj(a,b=0):
    return str(a+b)

# dodajemy typ parametru
def dodaj2(a: int=0,b: int=0):
    return str(a+b)

# informujemy opcjonalnie o typie zwracanym  -> str
def dodaj2(a: int=0,b: int=0) -> str:
    return str(a+b)

print(dodaj(1,2))
print(type(dodaj(1,2)))

print(dodaj(4))

# możemy wyświetlić obiekt funkci
print(dodaj2)
print(dodaj2.__str__())

# możemy wyświetlić nazwę funkcji
print(dodaj2.__name__)

innaFunkcja = dodaj
print(innaFunkcja(5,6))

# funkcja w funkcji
def generatorFunkcji(bezZmian, czyUpper):
    def powielTekst(tekst, ileRazyPowtorzyc = 1):
        return tekst * ileRazyPowtorzyc
    def powielTekstUpper(tekst: str, ileRazyPowtorzyc = 1):
        return tekst.upper() * ileRazyPowtorzyc
    def powielTekstLower(tekst, ileRazyPowtorzyc = 1):
        return tekst.lower() * ileRazyPowtorzyc

    if bezZmian:
        return powielTekst
    else:
        if czyUpper:
            return powielTekstUpper
        else:
            return powielTekstLower

funkcjaUpper = generatorFunkcji(False, True)
print(funkcjaUpper("abc", 5))