# Let's try to generate a histogram of some data using the Artist layer:

import matplotlib.pyplot as plt
import numpy as np

# create 10000 random numbers using numpy
x = np.random.randn(10000)

plt.hist(x, 100)
plt.title('Normal distribution with $\mu=0, \sigma=1$')
plt.savefig('./8. Data Visualization with Python/Module 1/matplotlib_histogram.png')
plt.show()
