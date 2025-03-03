class Book:
    def __init__(self,title = '',author = '',pages = 0):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Książka \"{self.title}\" napisana przez {self.author} \" liczba stron {self.pages}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.pages == other.pages

    # metoda nadpisująca sum
    def __radd__(self, other):
        if isinstance(other,Book):
            return self.pages + other.pages
        else:
            return self.pages +  other

    # metoda porównywania mniejsze
    def __lt__(self, other):
        if self.pages < other.pages:
            return True
        return False


ksiazka1 = Book("O mnie", "Ja", 99)
ksiazka2 = Book("O mnie", "Ja", 99)
ksiazka3 = Book("O mnie", "Ja", 101)

print(ksiazka1)
print(ksiazka1==ksiazka2)
print(ksiazka1==ksiazka3)
lista = [1,2,3]
print(sum(lista))
lista2 = [ksiazka1,ksiazka2,ksiazka3]
print(sum(lista2))
print((lista2))

if ksiazka1 < ksiazka2:
    print(f"Książka {ksiazka1} jest cieńsza niż książka {ksiazka2}")
else:
    print(f"Książka {ksiazka2} niejest cieńsza niż książka {ksiazka1}")
