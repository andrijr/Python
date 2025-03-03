# wyrażenia listowe
# [wyrażenie for element in kolekcja if warunek]

lista = []
for i in range(10):
    lista.append(i)
print(lista)

# 1 sposób
lista = []
for i in range(10):
    lista.append(10)
print(lista)

# 2 sposób
lista2 = [10] * 10
print(lista2)

napis = 'abc ' * 7
print(napis)

# 3 sposób
# wyrażenia listowe
# [wyrażenie for element in kolekcja if warunek]
lista3 = [10 for i in range(10)]
print(lista3)

lista3 = [i for i in range(10)]
print(lista3)

lista4 = [i for i in 'napis']
print(lista4)

lista5 = [int(i) for i in '12345']
print(lista5)

x, y = [int(liczba) for liczba in input('podaj dwie liczby po spacji: ').split()]
print(x, y)

lista6 = [int(liczba) for liczba in input('podaj dowolną ilośc liczb  po spacji: ').split()]
print(lista6)
