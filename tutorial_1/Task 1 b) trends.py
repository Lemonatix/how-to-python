from element import *
import matplotlib.pyplot as plt
import numpy as np

# Define the element groups
alkalines = [Li, Na, K, Rb, Cs, Fr]
earthalkalines = [Be, Mg, Ca, Sr, Ba, Ra]

# Define a function to plot the data points
def plot_data():
    plt.figure(figsize=(8, 6))
    
    # Plot alkalines
    for alms in alkalines:
        if alms.Electronegativity is not None and alms.AtomicRadius is not None:
            plt.scatter(alms.Electronegativity, alms.AtomicRadius, c='red', label='Alkalines' if alms == alkalines[0] else "")
    
    # Plot earthalkalines
    for ealms in earthalkalines:
        if ealms.Electronegativity is not None and ealms.AtomicRadius is not None:
            plt.scatter(ealms.Electronegativity, ealms.AtomicRadius, c='blue', label='Earth Alkalines' if ealms == earthalkalines[0] else "")

    plt.xlabel("Electronegativity")
    plt.ylabel("Atomic Radius")
    plt.legend()

# Define a function for manual fitting for alkalines
def manual_fit_alkaline(a, b):
    alkaline_electroneg = [elem.Electronegativity for elem in alkalines if elem.Electronegativity is not None]
    alkaline_radii = [elem.AtomicRadius for elem in alkalines if elem.AtomicRadius is not None]
    x_fit = np.linspace(min(alkaline_electroneg), max(alkaline_electroneg), 100)
    y_fit = a * x_fit + b
    plt.plot(x_fit, y_fit, color='red', linestyle='--', label=f'Alkaline Manual Fit (a={a}, b={b})')

# Define a function for manual fitting for earthalkalines
def manual_fit_earthalkaline(a, b):
    earthalkaline_electroneg = [elem.Electronegativity for elem in earthalkalines if elem.Electronegativity is not None]
    earthalkaline_radii = [elem.AtomicRadius for elem in earthalkalines if elem.AtomicRadius is not None]
    x_fit = np.linspace(min(earthalkaline_electroneg), max(earthalkaline_electroneg), 100)
    y_fit = a * x_fit + b
    plt.plot(x_fit, y_fit, color='blue', linestyle='--', label=f'Earth Alkaline Manual Fit (a={a}, b={b})')

# Plotting example usage
plot_data()  # Plot data points
manual_fit_alkaline(a=-420, b=550)  # Example values for a and b for alkalines
manual_fit_earthalkaline(a=-160, b=340)  # Example values for a and b for earthalkalines
plt.legend()
plt.show()
