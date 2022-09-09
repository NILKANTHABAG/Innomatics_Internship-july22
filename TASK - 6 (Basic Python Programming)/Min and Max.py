import numpy
N, M = map(int, input().split())
A = numpy.array([input().split() for _ in range(N)], int)
Min = numpy.min(A,axis = 1)
print(numpy.max(Min))
