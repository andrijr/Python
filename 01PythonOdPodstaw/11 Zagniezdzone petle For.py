for x in range(1,10):
    for y in range(1,10):
        print(x," x ", y, " = ", x*y)
    print("")
print("----")


for x in range(1,10):
    for y in range(1,10):
        print( x*y, end=" ")
    print("")
print("----")


# %-formatting
for x in range(1,10):
    for y in range(1,10):
        print( '%2s' % (x*y) , end=" ")
    print("")
print("----")


# str.format()
for x in range(1,10):
    for y in range(1,10):
        print( '{:2}'.format(x*y) , end=" ")
    print("")
print("----")