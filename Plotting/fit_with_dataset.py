import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def damped_sine(x, A, B, C, D, E):
    return A * np.exp(-B * x) * np.sin(C * x + D) + E

df = pd.read_csv("mydata.csv")

# 2. (Optional) Remove data points where y > 3.0
df_filtered = df[df["y"] <= 3.0].copy()  # comment out if you don’t want to remove anything

x_data = df_filtered["x"].to_numpy()
y_data = df_filtered["y"].to_numpy()

initial_guess = [1.0, 0.1, 1.0, 0.0, 0.0]

popt, pcov = curve_fit(damped_sine, x_data, y_data, p0=initial_guess)
A_fit, B_fit, C_fit, D_fit, E_fit = popt

perr = np.sqrt(np.diag(pcov))
A_err, B_err, C_err, D_err, E_err = perr

print("Fitted parameters (with optional filter y<=3.0):")
print(f"A = {A_fit:.4f} ± {A_err:.4f}")
print(f"B = {B_fit:.4f} ± {B_err:.4f}")
print(f"C = {C_fit:.4f} ± {C_err:.4f}")
print(f"D = {D_fit:.4f} ± {D_err:.4f}")
print(f"E = {E_fit:.4f} ± {E_err:.4f}")

# Plot the filtered data vs. the fitted function
x_fit = np.linspace(x_data.min(), x_data.max(), 300)
y_fit = damped_sine(x_fit, *popt)

plt.figure(figsize=(8,5))
plt.scatter(x_data, y_data, color='red', alpha=0.8, label='Filtered Data')
plt.plot(x_fit, y_fit, color='blue', label='Fitted Function', linewidth=2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Damped Sine Curve Fitting with Smaller Amplitude")
plt.legend()
plt.show()