import numpy

def arrays(arr):
    numpy_array = numpy.array(arr, float)
    return numpy_array[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)