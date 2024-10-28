# task 1
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

# task 2
from math import exp

def ionic_character(Element_A, Element_B):
    EN_A = Element_A.Electronegativity
    EN_B = Element_B.Electronegativity
    IC = 1 - exp(-0.25*(EN_A-EN_B)**2)
    return IC

def bond_polarity(Element_A, Element_B):
    EN_A = Element_A.Electronegativity
    EN_B = Element_B.Electronegativity
    ED = abs(EN_A - EN_B)
    return ED

# data from file experimental_data.py
deltaEs_exp = [0.305, 0.404, 0.505, 0.701, 0.903, 1.505, 1.904, 1.803, 1.699, 1.805, 2.005, 2.002, 2.105, 2.212, 2.31, 3.005, 3.202, 3.311]
ICs_exp = [0.03, 0.046, 0.073, 0.106, 0.17, 0.542, 0.45, 0.593, 0.751, 0.755, 0.728, 0.763, 0.748, 0.814, 0.743, 0.902, 0.857, 0.695]

bonds = ['I-Br','H-I','I-Cl','H-Br','H-Cl','H-F','Li-I','Li-Br','Li-I','K-I','Cs-I',
         'Li-Cl','Cs-Cl','Na-Cl','K-Br','K-Cl','Li-F','K-F','Cs-F']

ICs = []
BPs = []

for bond in bonds:
    El_A,El_B = bond.split('-')
    ICs.append(ionic_character(globals()[El_A], globals()[El_B]))
    BPs.append(bond_polarity(globals()[El_A], globals()[El_B]))

plt.plot(BPs, ICs, )
plt.scatter(deltaEs_exp, ICs_exp)
plt.show()