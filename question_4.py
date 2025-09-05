import numpy
import random
m = numpy.random.randint(0,100,size=(5,5))

print("Original: ", m)

mid = m[1:4, 1:4]

print("New: ", mid)

first = mid[0]
print("First row: ", first)

last = mid[2]
print("Last row: ", last)

dot = np.dot(first,last)
print("Dot product: ", dot)
