from element import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Define Mulliken Electronegativity calculation
def Mullikan_Electronegativity(el):
    if el.ElectronAffinity is not None and el.IonizationEnergy is not None:
        return (el.ElectronAffinity + el.IonizationEnergy) / 2
    return None

# Select elements of interest
selected_elements = [H, He, Na, Fe, Au, Ca, Y, Mg, Mn, F, Ag, O, N, Cl, Br, S, C]

# Prepare lists for class and Mulliken electronegativities
class_electronegs = []
mulliken_electronegs = []

for el in selected_elements:
    if el.Electronegativity is not None:
        class_electronegs.append(el.Electronegativity)
        mulliken_value = Mullikan_Electronegativity(el)
        if mulliken_value is not None:
            mulliken_electronegs.append(mulliken_value)

# Define linear transformation function for alignment
def linear_transform(mulliken_value, a, b):
    return a * mulliken_value + b

# Fit transformation to align Mulliken with class electronegativity
params, _ = curve_fit(linear_transform, mulliken_electronegs, class_electronegs)
a, b = params

# Apply transformation to Mulliken values
adjusted_mulliken_electronegs = [linear_transform(mul, a, b) for mul in mulliken_electronegs]

# Plot comparison of Adjusted Mulliken vs Class Electronegativity
plt.figure(figsize=(10, 6))
for el, adjusted_mul, class_en in zip(selected_elements, adjusted_mulliken_electronegs, class_electronegs):
    plt.scatter(class_en, adjusted_mul, label=el.name)
    plt.text(class_en, adjusted_mul, el.name, fontsize=7, ha='right')

# Reference line for perfect alignment
plt.plot([min(class_electronegs), max(class_electronegs)],
         [min(class_electronegs), max(class_electronegs)], 'k--', label='y=x (Perfect Alignment)')

plt.xlabel("Class Electronegativity")
plt.ylabel("Adjusted Mulliken Electronegativity")
plt.legend(fontsize=8)
plt.title("Mulliken Electronegativity vs Class Electronegativity")
plt.show()
