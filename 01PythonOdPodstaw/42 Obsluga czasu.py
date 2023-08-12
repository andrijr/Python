
import time
import datetime
import math

print(time.time()) # aktualny czas w sekundach
t = time.time()
lista = []
for x in range(0,10000000):
    lista.append(x**2)
print("czas wykonania ", time.time()-t)


t2 = time.time()
lista2 = []
for x in range(0,10000000):
    lista2.append(pow(x,2))
print("czas wykonania ", time.time()-t2)

# time.clock()
# lista3 = []
# for x in range(0,10000000):
#     lista3.append(pow(x,2))
# print("czas wykonania ", time.clock())

for x in range(0,10):
    print(x)
    time.sleep(0.3)

aktualnyCzas = datetime.datetime.now()
print(aktualnyCzas, aktualnyCzas.day, aktualnyCzas.month, aktualnyCzas.year)