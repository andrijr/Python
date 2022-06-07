# suma = 0
# iloczyn = 1
# for x in range(5,1000,5):
#     suma += x
#     iloczyn *= x
# print(suma)
# print(iloczyn)

#Program oblicza średnią arytmetyczną dowolnej ilości liczb
ileLiczb = int(input("Podaj z ilu liczb chcesz wyciągnąć średnią: "))
suma = 0
for x in range(0,ileLiczb):
    suma += int(input("Podaj kolejną liczbę: "))
print("Średnia arytmetyczna podanych liczb wynosi: ", suma/ileLiczb)

#Praca domowa:
#1. Napisz programy liczące: średnią harmoniczną, średnią geometryczną, średnią kwadratową
#2. Przeczytaj do czego służą te średnie
#3. Oblicz sumę liczb od 1 do 1000 - wszystkich, oraz tych, które są podzielne przez 3, a następnie oblicz sumę liczb niepodzielnych przez 3