def dodaj(a :int = 0,b :int = 0) -> str:
    return str(a+b)

print(dodaj(5))

print(dodaj.__name__)

innaFunkcja = dodaj
print(innaFunkcja(5,1))

def generatorFunkcji(bezZmian,czyUpper):
    def powielTekst(text,ileRazyPowtorzyc = 1):
        return text * ileRazyPowtorzyc
    def powielTekstUpper(text:str, ileRazyPowtorzyc = 1):
        return text.upper() * ileRazyPowtorzyc
    def powielTekstLower(text:str, ileRazyPowtorzyc = 1):
        return text.lower() * ileRazyPowtorzyc

    if bezZmian:
        return powielTekst
    else:
        if czyUpper:
            return powielTekstUpper
        else:
            return powielTekstLower

funkcjaUpper = generatorFunkcji(False,True)

print(funkcjaUpper("abc",5))