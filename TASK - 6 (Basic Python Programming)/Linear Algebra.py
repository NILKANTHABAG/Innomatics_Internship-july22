import numpy
N = int(input()) 
A = numpy.array([input().split() for _ in range(N)],float)
# Output needs to be round to 2 decimal points
print(round(numpy.linalg.det(A),2))
