class Book:
    def __init__(self,title = '',author = '',pages = 0):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Książka \"{self.title}\" napisana przez {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __radd__(self, other):
        if isinstance(other,Book):
            return self.pages + other.pages
        else:
            return self.pages + other

    def __lt__(self, other):
        if self.pages < other.pages:
            return True
        return False

ksiazka1 = Book("abc","dbe",123)
ksiazka2 = Book("xyz","zyx",987)
ksiazka3 = Book("eee","aaa",333)

lista = [ksiazka1,ksiazka2,ksiazka3]
print(sum(lista))

print(ksiazka1 == ksiazka2)

if ksiazka1 < ksiazka2:
    print(f"Książka {ksiazka1} jest cieńsza niż książka {ksiazka2}")
else:
    print(f"Książka {ksiazka2} jest cieńsza niż książka {ksiazka1}")