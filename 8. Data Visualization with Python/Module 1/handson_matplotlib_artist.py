# Let's try to generate a histogram of some data using the Artist layer:

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas # import FigureCanvas
from matplotlib.figure import Figure # import Figure artist

fig = Figure()
canvas = FigureCanvas(fig)

# create 10000 random numbers using numpy
import numpy as np
x = np.random.randn(10000)

ax = fig.add_subplot(111) # create an axes artist

ax.hist(x, 100) # generate a histogram of the 10000 numbers

ax.set_title('Normal distribution with $\mu=0, \sigma=1$')
fig.savefig('./8. Data Visualization with Python/Module 1/matplotlib_histogram.png')
