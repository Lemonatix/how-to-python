class Element:
    def __init__(self, massArgument: float, nameArgument: str, densityArgument: float):
        self.mass = mass
        self.name = name
        self.density = density

ElementList = []
element_masses = [1.00, 4.00, 6.94, 9.01, 10.81, 12.01, 14.00, 15.99, 18.99, 20.18]
element_densities = [0.8988e-4, 0.1785e-3, 0.534, 1.85, 2.34, 2.267, 0.12506e-2, 0.1429e-2, 0.1696e-2, 0.8999e-3]
element_names = ["Wasserstoff", "Helium", "Lithium", "Beryllium", "Bor", "Kohlenstoff", "Stickstoff", "Sauerstoff", "Fluor", "Neon"]

for name, mass, density in zip(element_masses, element_names, element_densities):
    tempElement = Element(name, mass, density)
    ElementList.append(tempElement)

a = [print(meinElement.name) for meinElement in ElementList]
b = [print(meinElement.mass) for meinElement in ElementList]
c = [print(meinElement.density) for meinElement in ElementList]


    



