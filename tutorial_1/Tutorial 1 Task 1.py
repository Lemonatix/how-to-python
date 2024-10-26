from element import *
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit # to install(in terminal): python -m pip install scipy 
import numpy as np

# for a)
print(dir()) # gives all attributes of the functions defined in element.py

# for b)
alkalines = [Li, Na, K, Rb, Cs, Fr]
earthalkalines = [Be, Mg, Ca, Sr, Ba, Ra]

for alms in alkalines:
    plt.scatter(alms.Electronegativity, alms.AtomicRadius, c = 'red')

for ealms in earthalkalines:
    plt.scatter(ealms.Electronegativity, ealms.AtomicRadius, c = 'blue')

plt.xlabel("Electronegativity")
plt.ylabel("Atomic Radius")
plt.legend()
plt.show()

# for c)
def Mullikan_Electronegativity(el):
    En_Mul = (el.ElectronAffinity + el.IonizationEnergy)/2
    return En_Mul

selected_elements = [H, He, Na, Fe, Au, Ca, Y, Mg, Mn, F, Ag, O, N, Cl, Br, S, C]

for el in selected_elements:
    En_Mul = Mullikan_Electronegativity(el)
    plt.scatter(el.Electronegativity, En_Mul) # values do not align, see Millikan alignment.py

plt.title("Electronegativity against Mullikan Electronegativity")
plt.xlabel("Elektronegativity")
plt.ylabel("Mullikan Elektronegativity")
plt.show()