class Element:
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

elemList = []
for element_masses, element_names, element_densities in zip(element_masses, element_names, element_densities):
    tempElement = Element(element_masses, element_names, element_densities)
    elemList.append(tempElement)