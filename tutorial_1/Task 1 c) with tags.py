
from element import *
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit # to install(in terminal): python -m pip install scipy 
import numpy as np

alkalines = [Li, Na, K, Rb, Cs, Fr]
earthalkalines = [Be, Mg, Ca, Sr, Ba, Ra]

def Mullikan_Electronegativity(el):
    if el.ElectronAffinity is not None and el.IonizationEnergy is not None:
        return (el.ElectronAffinity + el.IonizationEnergy) / 2
    return None  # return nothing if either attribute is missing

selected_elements = [H, He, Na, Fe, Au, Ca, Y, Mg, Mn, F, Ag, O, N, Cl, Br, S, C]

for el in selected_elements:
    En_Mul = Mullikan_Electronegativity(el)
    if En_Mul is not None and el.Electronegativity is not None:  # Only plot if values are available, because some are None
        plt.scatter(el.Electronegativity, En_Mul)
        plt.text(el.Electronegativity, En_Mul, el.name, fontsize=9, ha='right') 

plt.title("Electronegativity against Mullikan Electronegativity")
plt.xlabel("Electronegativity")
plt.ylabel("Mullikan Electronegativity")
plt.show()
