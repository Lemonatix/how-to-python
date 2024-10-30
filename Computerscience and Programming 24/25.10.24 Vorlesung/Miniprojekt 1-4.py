class Element:
    def __init__(self, name: str, mass: float):
        self.name = name
        self.mass = mass

a = Element("Wasserstoff", 2.03)
b = Element("Helium", 4.12)
c = Element("Beryllium", 6.02)
d = Element("Wrongium", -3)

x = 10

def f(arg1):
    value = 3+2*arg1
    return value # value is not defined without return value

y = f(x) # if y = value: value ist ein lokale variable: sie ist außerhalb von f nicht sichtbar für den interpreter => return-Funktion notwendig
print(y)

u=f(100)
print(u)

value1 = 0
def f(arg2):
    global value1
    value1 = 3 + 3*arg2

x = 5
f(x)
print(value1)

z = 10 # falls nicht definiert: NameError
def f(arg3):
    value = 3 + 2*arg3 # wenn statt arg 3 = z: statt 43 ist Ergebnis wieder 23, da x = z
    return value

r=f(20)
print(r) # ergibt wieder 23

def f(x, m=2, a=3):
    return a + m*x

y = f(20)
print(y)

def int(self, massArgument: float, nameArgument: str, densityArgument: float):
    self.mass = massArgument
    self.name = nameArgument
    self.density = densityArgument

def molar_density(self) -> float:
    molar_mass = self.mass_u # 1u = g/mol
    return self.density / molar_mass

def mass_for_mol(self, moles: float) -> float:
    molar_mass = self.mass_u
    return moles * molar_mass

element_names = ["Wasserstoff", "Helium", "Lithium", "Beryllium", "Bor", "Kohlenstoff", "Stickstoff", "Sauerstoff", "Fluor", "Neon"]
print(element_names[0])
print(element_names[-1]) # prints the first entry of the list from the end
print(element_names[4:7]) # prints entries 5, 6, and 7, therefore everything after 4
print(element_names[4:7:2]) # prints entries 5, 7

Index = 4 # 5th Element is Bor, since python counts from 0
print("Das " + str(Index+1) + "te Element ist " + element_names[Index])

a = "Muenchen"
print(a*10) # der String "muenchen" wir zehnmal aneinander geprintet

element_masses = [1.00,4.00,6.94,9.01,10.81,12.01,14.00,15.99,18.99,20.18]
element_densities = [0.8988e-4, 0.1785e-3, 0.534, 1.85, 2.34, 2.267, 0.12506e-2, 0.1429e-2, 0.1696e-2, 0.8999e-3]

print(element_names.index("Bor"))
print(element_names.__len__()) # ist die Länge der Liste element_names

popped = element_names.pop(element_names.index("Bor"))
print(popped)
print(element_names) # Bor ist hier exkludiert, da popped
print(element_names.__len__())

element_names.append(popped) # instead of popped in the parantheses: element_names.append("Bor") is also possible and has the same effect
print(element_names)
print(element_names.__len__())


lol = [element_names, element_masses, element_densities]
print(lol[2][5])
C = [lol[1][5], lol[0][5]]
print(C)

CbutasDict = dict(name = lol[0][5], mass = lol[1][5], density = lol[2][5])
print(CbutasDict["name"])

namesIterator = iter(element_names)
massIterator = iter(element_masses)
densityIterator = iter(element_densities)

vorname = next(namesIterator) # unnötig langer code, der durch for-Schleife obsolet wird
zweiterName = next(namesIterator)
dritterName = next(namesIterator)

firstMass = next(massIterator)
secondMass = next(massIterator)
thirdMass = next(massIterator)

firstDensity = next(densityIterator)
secondDensity = next(densityIterator)
thirdDensity = next(densityIterator)

namesIterator = iter(element_names) 
for currentValue in namesIterator: # die oben gennannte for-Schleife
    print(currentValue)

for name, mass in zip(element_names, element_masses):
    print("Das Element " + name + " hat die Masse " + str(mass), " u")