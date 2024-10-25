from element import *
import matplotlib.pyplot as plt
# Task 1
# a)
print(dir(H))

# b)
ams = [Li, K, Na, Rb, Cs]
eams = [Be, Mg, Ca, Sr, Ba]
for am in ams:
    plt.scatter(am.Electronegativity, am.AtomicRadius, c = 'red')
for eam in eams:
    plt.scatter(eam.Electronegativity, eam.AtomicRadius, c = 'yellow')
plt.show()

# c)

def Mulliken_electronegativity(el):
    
    EN_mulliken = (el.ElectronAffinity + el.IonizationEnergy)/2

    return EN_mulliken

element_list = [H, C, O, F, Cl, Br, Cu, Mn, Pt, Au, Fe, B, Ir, As, S, P]

for el in element_list:

    EN_mulliken = Mulliken_electronegativity(el)

    plt.scatter(el.Electronegativity, EN_mulliken)
plt.title('Electronegativity vs. Mulliken Electronegativity')
plt.show()

def Mulliken_to_Pauling(EN_mulliken):

    EN_mulliken_eV = EN_mulliken/96.485
    
    EN_Pauling = 1.35 * EN_mulliken_eV**0.5 - 1.37
    
    
    return EN_Pauling


for el in element_list:

    EN_mulliken = Mulliken_electronegativity(el)

    EN_pauling = Mulliken_to_Pauling(EN_mulliken)
    
    plt.scatter(el.Electronegativity, EN_pauling)
    
plt.title('Electronegativity vs. converted Mulliken Electronegativity')
plt.show()


# Task 2
# a)

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