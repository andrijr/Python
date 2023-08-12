
def dodawanie(a , b):
    print("wynik", a+b)

dodawanie(5, 6)


# typ argumentu funkcji jet tylko informacją nie wymuszeniem zadziała nawet tekst bo zależy od tego jak funkcja zbudowana
def dodawanie(a: int, b: int):
    print("wynik", a+b)

dodawanie(5, 6.2)