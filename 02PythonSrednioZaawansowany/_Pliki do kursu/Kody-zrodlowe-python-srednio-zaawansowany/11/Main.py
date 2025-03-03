# x = None
#
# y = int(input("Podaj wartość dla x: "))
# if y > 0:
#     x = y

# if x is not None:
#     print(x)

def f(x):
    if x > 0:
        return True
    elif x < 0:
        return False
    else:
        pass

a = f(2)
b = f(-2)
c = f(0)

print(f"a:{a}, b:{b}, c:{c}")