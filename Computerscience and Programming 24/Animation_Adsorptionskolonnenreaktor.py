import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialisierung der Matrix
concentration = np.zeros([100, 100])
concentration[0, :] = 1
temp_mat = np.zeros([100, 100])

# Daten für Animation sammeln
frames = []

for steps in range(50): # Anzahl der iterierten Diffusionsschritte
    for i in range(100):
        for j in range(100):
            temp = 0
            if i-1 >= 0:
                temp += concentration[i-1, j]
            if i+1 < 100:
                temp += concentration[i+1, j]
            if j-1 >= 0:
                temp += concentration[i, j-1]
            if j+1 < 100:
                temp += concentration[i, j+1]
            temp_mat[i, j] = 0.25 * temp
    concentration = temp_mat
    concentration[0, :] = 1
    frames.append(concentration.copy()) # 1 Frame = 1 Step

# Animation erstellen
fig, ax = plt.subplots() # erstellt subplots
im = ax.imshow(frames[0][1:, :], cmap='viridis', aspect='auto') # erstellt Bild 

def update(frame): # aktualisiert die Bilder bzgl. den gesammelten frames (Liste)
    im.set_data(frame[1:, :])
    return[im]

ani = FuncAnimation(fig, update, frames=frames, interval=100, blit=True) # erstellt Animation, bzw. Bilder werden hintereinander abgespielt
plt.colorbar(im, ax=ax, label="Concentration")
plt.show()