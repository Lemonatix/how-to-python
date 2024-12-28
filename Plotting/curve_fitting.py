import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def func(x, a, b, c):
    return a * x**2 + b * x + c

np.random.seed(0) # keeps data the same each time

x_data = np.linspace(-5, 5, 50)
y_true = func(x_data, 2.0, -1.0, 5.0) # true parameters: a = 2, b = -1 c = 5
y_data = y_true + np.random.normal(scale=2.0, size = x_data.shape) # add some noise

# use curve_fit to find optimal parameters = popt
# and estimated covariance of parameters = pcov

popt, pcov = curve_fit(func, x_data, y_data, p0=[1, 1, 1]) # p0 is initial guess

# extract fitted parameters
a_fit, b_fit, c_fit = popt

print(f"The fitted parameters are: a = {a_fit}, b = {b_fit}, c = {c_fit}")

plt.figure(figsize=(8, 5))
plt.scatter(x_data, y_data, label="Noisy Data", color="red", alpha=0.5)
plt.plot(x_data, y_true, label="True Function", color="green")
plt.plot(x_data, func(x_data, *popt), label="Fitted Function", color="blue")
plt.legend()
plt.title("Curve Fitting Example")
plt.xlabel("x")
plt.ylabel("y")
plt.show()