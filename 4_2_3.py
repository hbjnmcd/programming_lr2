import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(-x)

def g(x):
    return np.cos(x)

def h(x):
    return np.exp(x)

x = np.linspace(0, 2*np.pi, 100)

plt.figure(1)

plt.subplot(221)
plt.plot(x, f(x))
plt.title('График функции sin(-x)')

plt.subplot(222)
plt.plot(x, g(x))
plt.title('График функции cos(x)')

plt.figure(2)

plt.plot(x, h(x))
plt.title('График функции e^(x)')

plt.show()
