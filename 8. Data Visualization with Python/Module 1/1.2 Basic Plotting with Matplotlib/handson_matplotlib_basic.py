import matplotlib as mpl
import matplotlib.pyplot as plt

print('matplotlib version: ', mpl.__version__)

plt.plot(5,5, 'o')

plt.ylabel("Y")
plt.xlabel("X")
plt.title("Plotting Example")

plt.show()