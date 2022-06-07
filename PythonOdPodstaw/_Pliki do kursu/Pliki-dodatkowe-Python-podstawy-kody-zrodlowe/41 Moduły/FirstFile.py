import Module

aList = []
number = int(input("Podawaj liczby całkowite na których chcesz operować. Jeżeli chcesz zakończyć wpisz 0: "))
while number != 0:
    aList.append(number)
    number = int(input("Podawaj liczby całkowite na których chcesz operować. Jeżeli chcesz zakończyć wpisz 0: "))

print("Iloczyn wynosi", Module.multiply(aList))