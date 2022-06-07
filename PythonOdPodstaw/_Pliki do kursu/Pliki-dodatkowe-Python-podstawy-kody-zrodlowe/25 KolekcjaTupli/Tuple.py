exampleTuple = ("Obiekt 1", 2, 3, 4.5, "Obiekt 5")
newTuple = exampleTuple + ("Obiekt 6",)
print(exampleTuple)
print(id(exampleTuple))
print(newTuple)

# for element in newTuple:
#     print(element)

exampleTuple = exampleTuple + ("Kolejny obiekt",)
print(exampleTuple)
print(id(exampleTuple))

print(exampleTuple[3])

str = "napis"
print(str[1])