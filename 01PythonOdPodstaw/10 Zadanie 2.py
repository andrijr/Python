# Napisz programy
# oblicz sume liczb od 1 do 1000 wszystkich oraz tych które są podzielne przez 3
# następnie oblicz sumę liczb niepodzielnych przez 3

print("suma liczb podzielnie przez x i suma niepodzielna przez x :")
n = int(input("podaj przez jaką liczbę podzielność: "))
sumaPodzielna = 0
sumaNiePodzielna = 0
for x in range(1, 1001):
    if x % n == 0:
        sumaPodzielna += x
        #print (x)
    else:
        sumaNiePodzielna += x
print("suma podzielna przez: ", n, " = ", sumaPodzielna)
print("suma niepodzielna przez: ", n, " = ", sumaNiePodzielna)


