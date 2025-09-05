import numpy
import random
m = numpy.random.randint(0,100,size=(5,5))

print(m)

min_m = m.min()
max_m = m.max()
mean_m = m.mean()
norm = (m - min_m)/(max_m - min_m)

print(norm)


