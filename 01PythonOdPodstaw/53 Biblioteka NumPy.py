import numpy

matrix1 = numpy.array([[1,2], [3,4]])
matrix2 = numpy.array([[1,2], [3,4]])
matrix3 = matrix2 + matrix1


print(matrix1)
print(matrix1.shape)
print(matrix1 + matrix2)
print(matrix1 * matrix2)
print(list(matrix1 + matrix2))
print(list(matrix3.flat))


def f(x,y):
    return x * y

matrix4 = numpy.fromfunction(f, (5,6), dtype=int)
print(matrix4)

def f2(x,y):
    return 1 + (x +1) * (y +1)

matrix5 = numpy.fromfunction(f2, (10,10), dtype=int)
print(matrix5)

matrix6 = numpy.array([[1,2], [3,4]], dtype=complex)
print(matrix6)

lista = list(numpy.linspace(0,10,4))
print(lista)

n
print(matrix6)