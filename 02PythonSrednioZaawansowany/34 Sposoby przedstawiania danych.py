import math

import matplotlib.pyplot as plt
import numpy as np


listaX = [1,3,5,7,9]
listaY = [2,4,6,8,10]

plt.plot(listaX)
plt.show()


listaX = [1,3,5,7,9]
listaY = [2,4,18,8,12]

plt.plot(listaX, listaY)
plt.show()

listaX =[]
listaY =[]
for i in range(100):
    listaX.append(i/10)
    listaY.append(math.sin(i/10))
plt.plot(listaX, listaY, 'g')
plt.show()