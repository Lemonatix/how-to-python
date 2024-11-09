import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative

x = np.linspace(-5, 5)

def function(x):
    return x**3

def derivate(x):
    return derivative(function, x)

plt.plot(x, function(x))
plt.plot(x, derivate(x))
plt.show()


import numpy as np
import matplotlib.pyplot as plt
x = np.array([0.0, 1.0, 2.0, 3.0, 4.0, 4.9, 5.05, 5.15, 5.25, 5.35, 5.55, 5.65, 6.05, 6.55, 7.05, 7.55, 8.05, 8.55, 9.05, 9.6, 9.85, 10.1, 10.25, 10.35, 10.5, 10.85, 11.2, 11.9, 12.7, 13.5
])
y=np.array([2.48, 2.57, 2.72, 2.92, 3.21, 3.85, 4.59, 5.31, 5.64, 5.85, 6.14, 6.48, 6.72, 6.90, 7.08, 7.24, 7.40, 7.62, 7.97, 8.23, 8.36, 8.75, 9.52, 10.02, 10.31, 10.64, 10.87, 11.13, 11.29, 11.41
])
dy = np.gradient(y, x)

plt.plot(x, y)
plt.plot(x, dy)
plt.show()