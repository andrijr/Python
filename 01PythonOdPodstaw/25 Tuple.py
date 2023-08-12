# różnica między tuple a lista jest taka że tuple są nie modyfikowalne
# tuple działa trochy szybciej od listy
# string jest przykładem tupli a nie listy
# tuple = krotka

tupla = ()
print(tupla)

tupla = tuple()
print(tupla)



tupla = ("a", 5, 6, 8, 6, "c")
print(tupla)
print(type(tupla))
tupla = tupla + ("s", 5.2)
tupla = tupla + ("z", ) # jeżeli dodajemy jeden element musimy dać przecinek po 1 elemencie
print(tupla)

for x in tupla:
    print(x)


