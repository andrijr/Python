
def rekurencyjneMnozenie(x, y):
    if y == 0:
        return 0
    return x + rekurencyjneMnozenie(x, y -1)

def rekurencyjneMnozenie2(x, y):
    if y == 0:
        return 0
    if y > 0:
        return x + rekurencyjneMnozenie(x, y - 1)
    if y < 0:
        return x + rekurencyjneMnozenie(x, y + 1)


print(rekurencyjneMnozenie(5, 4))