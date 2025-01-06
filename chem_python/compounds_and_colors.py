from fpdf import FPDF

pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.set_font("Arial", style='B', size=16)
pdf.cell(200, 10, txt="List of Chemical Compounds and Their Colors", ln=True, align='C')
pdf.ln(10) 

pdf.set_font("Arial", style='B', size=12)
pdf.cell(80, 10, "Chemical Formula", 1, 0, 'C')
pdf.cell(110, 10, "Color", 1, 1, 'C')

chemical_data = [
    ("Cr2O3", "Green"),
    ("Fe2O3", "Red-Brown"),
    ("CuSO4", "Blue"),
    ("KMnO4", "Purple"),
    ("PbI2", "Yellow"),
    ("ZnO", "White (when cold), Yellow (when hot)"),
    ("AgCl", "White"),
    ("AgBr", "Pale Yellow"),
    ("AgI", "Yellow"),
    ("NiSO4", "Green"),
    ("CoCl2", "Pink"),
    ("Cu(NO_3)2", "Blue-Green"),
    ("MnO2", "Black"),
    ("K2Cr2O7", "Orange"),
    ("BaSO4", "White"),
    ("PbCrO4", "Yellow"),
    ("Cu2O", "Red"),
    ("HgS", "Red or Black"),
    ("Fe3O4", "Black"),
    ("CaCO3", "White"),
    ("Pb3O4", "Red"),
    ("TiO2", "White"),
    ("K2CrO4", "Yellow"),
    ("MnSO4", "Pale Pink"),
    ("CuSO4", "Blue (anhydrous: White)"),
    ("MnCl2", "Pink"),
    ("NaCl", "White"),
    ("Na2SO4", "White"),
    ("PbO2", "Brown"),
    ("K3PO4", "White"),
    ("FeCl3", "Yellow"),
    ("Co(NO3)2", "Red"),
    ("NiCl2", "Green"),
    ("Al2O3", "White"),
    ("SnO2", "White"),
    ("V2O5", "Yellow-Orange"),
    ("HgO", "Red or Yellow"),
]

pdf.set_font("Arial", size=12)
for formula, color in chemical_data:
    pdf.cell(80, 10, formula, 1, 0, 'C')
    pdf.cell(110, 10, color, 1, 1, 'C')

file_path = "/home/mmr/how-to-python/All_Chemical_Compounds_and_Colors.pdf"
pdf.output(file_path)