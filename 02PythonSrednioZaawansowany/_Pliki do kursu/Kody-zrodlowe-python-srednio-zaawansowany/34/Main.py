import pylab
import math

listaX = []
listaY = []
for i in range(100):
    listaX.append(i/10)
    listaY.append(math.sin(i/10))

pylab.plot(listaX,listaY,'go')
pylab.show()