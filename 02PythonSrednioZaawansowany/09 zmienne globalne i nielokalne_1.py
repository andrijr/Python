# funkcje można zagłębiać i zagnieżdżać
# robić funkcje w funkcji
# w klasie może być funkcja w tej funkcji funkcja a w tej funkcji klasa - nie jest to często używane

def f1(x):
   #x = 4
    print("Funkcja f x = ", x)
    def g(y):
        x = 7 # x1
        print("Funkcja g y = ", y)
        print("x = ", x)
    x += 1
    g(x)
    print("x = ", x) # x2

# x1 i x2 to są dwa różne x. x2 to nowy x o tej samej nazwie co x1
f1(2)


print("funkcja 2")
def f2(x): # ten x tutaj jest lokalny
   #x = 4
    print("Funkcja f x = ", x)
    def g(y):
        nonlocal x
        x = 7 # x1 tutaj x jest globalny
        print("Funkcja g y = ", y)
        print("x = ", x)
    x += 1
    g(x)
    print("x = ", x) # x2

# x1 i x2 to są dwa różne x. x2 to nowy x o tej samej nazwie co x1
f2(2)


