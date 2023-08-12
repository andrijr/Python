i = 3
if i > 0:
    print(i)
print("----")

licznik = 0
for i in range(1,101):
    if i % 17 == 0:
        licznik += 1
        print("podzilana przez 17: ", i)
        if i % 2 == 0:
            licznik += 1
            print("podzielna przez 17 i 2: ", i)
print("liczba wystąpień: ", licznik)
print("----")

for x in range(1, 10):
    for y in range(1,10):
        print('{:3}'.format(x*y), end="")
    print("")
print("----")


for x in range(1, 10):
    for y in range(1,10):
        if x*y < 100:
            print(' ', end="")
        if x*y < 10:
            print(' ', end="")
        print(' ' + str(x*y), end="")
    print("")
print("----")