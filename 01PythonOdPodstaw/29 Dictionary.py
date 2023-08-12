#  w słowniku nie odwał


slownik = {}
print(slownik)
print(type(slownik))

slownik = dict()
print(slownik)
print(type(slownik))

# slownik = {'klucz': wartość}
# slownik = {'key': value }

slownik = {"Andrij": 111, "Tomek": 222, "Agni": 444, "Jas": 333, "kot": [1, 3, 3]}
print(slownik)
print(slownik["Agni"])
slownik["Agni"] = 'tak'
print(slownik)
slownik["Anastazja"] = 777
print(slownik) 