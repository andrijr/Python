
tekst = "to jest nasz tekst"
zbiorTekstu = set(tekst).difference(" ")
print(zbiorTekstu)
slownik = dict((letter, tekst.count(letter)) for letter in zbiorTekstu)
print(slownik)
uporzadkowanaLista = sorted(slownik.keys())
print(uporzadkowanaLista)
for letter in uporzadkowanaLista:
    print(letter, slownik[letter])


# urzywaj komentarze ale nie za często jedynie tam gdzie to jest konieczne
# nazywaj obiekty żeby coś znaczyły
# urzywaj tego samego stylu nie nazywaj raz po angielsku raz po polsku
# jeżeli funkcja ma więcej jak 10 linij kodu zastanów się czy nie należy ją skrócić
# eliminój powtarzające się elementy
