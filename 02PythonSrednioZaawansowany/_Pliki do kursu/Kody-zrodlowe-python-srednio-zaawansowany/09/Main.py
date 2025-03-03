# def f(x):
#     print("Funkcja f")
#     def g(y):
#         nonlocal x
#         x = 7
#         print("Dostałem", y)
#         print(x)
#     x += 1
#     g(x)
#     print(x)

# x = 3
#
# def f():
#     y = 2
#     def g():
#         nonlocal y
#         y += 1
#         print(y)
#     g()
#     print(y)
#

zmienna = 10
def a():
    zmienna = 11
    def b():
        global zmienna
        zmienna = 12
    b()
    print(zmienna)

a()
print(zmienna)

x = [1,2,3]
y = x
x.append(4)
print(y)

print('Ala {x} kota')