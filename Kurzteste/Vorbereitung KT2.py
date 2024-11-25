import numpy as np
import matplotlib.pyplot as plt

# für Diagonalen
mat = np.zeros([10, 10])
for i in range(10):
    for j in range(10):
        if i == j+1 or i+1 == j:
            mat[i, j] = 1
print(mat)

# für bestimmte Positionen
mat1 = np.zeros([5, 5])
positions = [(0,0),(1,2),(3,4), (4,3), (2,1)]
for pos in positions:
    mat1[pos] = 1
print(mat1)

# generierst graues Rauschbild
n,m,k = 256, 256, 3
mat2 = np.zeros([n,m,k])
for n_ in range(n):
    for m_ in range(m):
        mat2[n_,m_,:] = np.random.rand(1) # mit k = 3 ist das ein RGB Bild

plt.imshow(mat2)
plt.show() # falls keine ipynb Datei 

# ein Beispiel für eine Klasse
class Laptop():
    def __init__(self, name, processor, ssd, ram, cost):
        self.name = name
        self.processor = processor
        self.ssd = ssd
        self.ram = ram
        self.cost = cost

    def details(self):
        print('The details of the laptop are:')
        print('Name         :', self.name)
        print('Processor    :', self.processor)
        print('SDD Capacity :', self.ssd)
        print('RAM          :', self.ram)
        print('Cost($)      :', self.cost)

laptop1 = Laptop('Thinkpad X1', 'Intel Core i9', 512, 16, 2000.00)
laptop1.details()

laptop2 = Laptop("MacBook Pro", "M2 Pro", 1000, 16, 2500.0)
laptop2.details()