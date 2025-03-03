from Foo_08_1 import Foo

# pola statyczne widoczne z poziomu klasy
# tworzenie takich pól morzemy robić w trakcie działania programu

Foo.x = 1
print(Foo.x)
# x jest teraz polem statycznym tak jakby wpisanym w klasie.
# różnica jest taka że nie możemy się dostać wewnątrz klasy bo klasa o tym nic nie wie.
# najczęściej jednak chcemy dodawać statyczne pola w obrębie klasy

obiekt = Foo()
obiekt.y = 2
print(obiekt.y)
# y jest teraz polem obiektu
# x jest polem statycznym a y jest polem obiektu

print("obiekt2 ----")
obiekt2 = Foo()
print(Foo.pole)
print(obiekt2.pole)

# w tym miejscu tworzymy kolejna zmienną instancyjną o tej samej nazwie co pole statyczne w klasie Foo
obiekt2.pole = 5

print(Foo.pole)
print(obiekt2.pole)

print("obiekt3 ---")
obiekt3 = Foo()
#print(obiekt3.a) # nie używamy tak powwinnismy kożystać z metod dostępowych cyyba że ustawimy a = property(get_a, set_a)
# możemy odnosić się bezpośrednio ale powinniśmy się odnosić przy pomocy metod dostępowych get i set

print(obiekt3.get_a())
obiekt3.a = 7
obiekt3._a = 9
print("----")
print(obiekt3.a)
print(obiekt3._a)
print(obiekt3.get_a())
obiekt3.a
