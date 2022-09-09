import numpy
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
Sum = numpy.sum(A,axis = 0)
Prod = numpy.prod(Sum,axis = 0)
print(Prod)