# zmienne globalne
# zmienne lokalne
# zmienne nielokalne

# dwie różne zmienny o tej samej nazwie przesłaniają się

x = 3 # zmienna globalna
def f1(x):
    x = 1
    print("x funkcji = ", x)

f1(2)
print("x globalny = ", x)



print("funkcja 2")
x = 3 # zmienna globalna
def f2():
    global x
    x = 1
    print("x funkcji = ", x)

f2()
print("x globalny = ", x)


x = 3
print("funkcja 3")
def f3():
    y = 2
    def g():
        nonlocal y # sprawdza czy jest y powyżej w pierwszym zagnieżdżeniu
        y += 1
        print("y = ", y)
    g()
    print("y = ", y)

f3()
print("x globalny = ", x)


print("funkca a")
zmienna = 10
def a():
    zmienna = 11
    def b():
        zmienna = 12
    b()
    print("zmienna = ", zmienna)

a()
print(zmienna)

print("funkca a1")
zmienna = 10
def a1():
    zmienna = 11
    def b1():
        nonlocal zmienna
        zmienna = 12
    b1()
    print("zmienna = ", zmienna)

a1()
print(zmienna)


print("funkca a2")
zmienna = 10
def a2():
    zmienna = 11
    def b2():
        global zmienna
        zmienna = 12
    b2()
    print("zmienna = ", zmienna)

a2()
print(zmienna)