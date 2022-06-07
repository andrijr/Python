def recursive_mult(x, y):
    if y == 0:
        return 0
    if y > 0:
        return x + recursive_mult(x, y - 1)
    else:
        return x + recursive_mult(x, y + 1)

x = int(input("Podaj pierwszą liczbę całkowitą: "))
y = int(input("Podaj drugą liczbę całkowitą: "))

print(recursive_mult(x, y))
