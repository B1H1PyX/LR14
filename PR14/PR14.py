import numpy as np
import matplotlib.pyplot as plt
def func(x):
    return 5 * np.sin(10 * x) * np.sin(3 * x) / np.sqrt(x)
x = np.linspace(1, 7, 100)
y = func(x)
plt.plot(x, y, linestyle='-', color='blue', linewidth=2, label='Y(x)=5*sin(10*x)*sin(3*x)/(x^(1/2))')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()