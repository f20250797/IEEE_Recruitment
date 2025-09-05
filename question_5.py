import numpy as np
import matplotlib.pyplot as plot

data = np.random.normal(loc=0, scale=1, size=1000)
plot.scatter(range(1000), data, alpha=0.6)
plot.xlabel("index")
plot.ylabel("value")
plot.title("plot of 1000 random no.")
plot.show()
