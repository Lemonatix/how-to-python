### Miniprojekt 6
class Element:
    def __init__(self, massArgument: float, nameArgument: str, densityArgument: float):
        self.mass = massArgument
        self.name = nameArgument
        self.density = densityArgument

def molar_density(self) -> float:
    molar_mass = self.mass_u # 1u = g/mol
    return self.density / molar_mass

def mass_for_mol(self, moles: float) -> float:
    molar_mass = self.mass_u
    return moles * molar_mass

element_masses = [1.00,4.00,6.94,9.01,10.81,12.01,14.00,15.99,18.99,20.18]
element_densities = [0.8988e-4, 0.1785e-3, 0.534, 1.85, 2.34, 2.267, 0.12506e-2, 0.1429e-2, 0.1696e-2, 0.8999e-3]
element_names = ["Wasserstoff", "Helium", "Lithium", "Beryllium", "Bor", "Kohlenstoff", "Stickstoff", "Sauerstoff", "Fluor", "Neon"]

elemList = []
for mass, name, density in zip(element_masses, element_names, element_densities):
    tempElement = Element(mass, name, density)
    elemList.append(tempElement)

for i in range(3):
    print(i)

for i,mass in enumerate(element_masses): 
    print("Das " + str(i) + "-te Element hat eine Masse von " + str(mass))

m1, d1, n1 = [5.04, 2.3, "Blablonium"]
m2, d2, n2 = [3.04, 1.3, "Schablonium"]
m1, m2 = m2, m1
print(m1, m2)

def convertTemperature(kelvin: float) -> float:
    if kelvin > 0:
        F = (kelvin - 273.15) * 9/5 + 32
        C = kelvin + 273.15
        return F, C 
    else:
        raise ValueError

freiTemp, euroTemp = convertTemperature(70)
_, euroTemp = convertTemperature(70)

try:
    freiTemp, euroTemp = convertTemperature(-300)
except ValueError:
    print("Die für Kelvin angegebene Wert war fehlerhaft")

### Miniprojekt 7
names = []
for name in element_names:
    if name[-1] == "n":
        names.append(name)
    else:
        pass

names = [name for name in element_names] # ist dasselbe wie oben
names = [name for name in element_names if name[-1] == "n"]

### Miniprojekt 8
import numpy as np
from numpy import * # beide Wege funktionieren, um das ganze Package zu importieren
import matplotlib.pyplot as plt # oder: from matplotlib import pyplot as plt

print(np.cos(np.pi))

x = np.linspace(0, 10, 100) # erzeugt 100 gleimäßig verteilte Werte zwischen 0 und 10
y = 3 + 2*x

plt.plot(x, y) # defineirt die Achsen des Plots
plt.show() # lässt den Plot anzeigen

lol = [element_names, element_masses, element_densities]
lol = np.array(lol) # List of Lists sei nun ein Numpy-Array

print(lol[:, 2]) # printet alle 3. Werte der Listen in der List of Lists
print(lol[2, :]) # printet die 2. List in der List of Lists, also densities: element_names = 0, element_masses = 1, element_densities = 2

lab1 = [23.1, 23.2, 23.0, 24.3, 21.1, 23.15, 23.01, 23.13] # 1 day = 1 value
lab2 = [23.00, 23.1, 29.1, 24.2, 21.0, 23.0, 22.99, 23.00] 
lab3 = [23.2, 23.5, 21.1, 26.7, 20.4, 22.15, 24.01, 23.44]

data = np.array([lab1, lab2, lab3])
print(data)

### Miniprojekt 9: Einfache Statistik
avg_per_day = np.mean(data, axis=0)
avg_per_lab = np.mean(data, axis=1)

# Plotting
plt.figure(figsize=(10, 5))
days = np.arange(1, len(avg_per_day) + 1)  # Day labels on x-axis

plt.plot(days, avg_per_day, marker='o', linestyle='-', color='blue', label='Average per Day')
plt.xlabel("Days")
plt.ylabel("Average Temperature (°C)")
plt.title("Average Temperature per Day")
plt.grid(True)
plt.legend()

# Separate plot for lab averages
plt.figure(figsize=(5, 5))
labs = ['Lab 1', 'Lab 2', 'Lab 3']
plt.bar(labs, avg_per_lab, color='red', label='Average per Lab')
plt.xlabel("Labs")
plt.ylabel("Average Temperature (°C)")
plt.title("Average Temperature per Lab")
plt.grid(True)
plt.legend()
plt.show()