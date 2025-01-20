import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# helper function
def plot_sphere(ax, center, radius=0.5, color='C0', alpha=1.0, resolution=12):
    """
    Zeichnet eine Kugel mit Mittelpunkt 'center' und Radius 'radius'
    in das 3D-Plot 'ax' (Axes3D).
    """
    u = np.linspace(0, 2*np.pi, resolution)
    v = np.linspace(0, np.pi, resolution)
    
    x = center[0] + radius * np.outer(np.cos(u), np.sin(v))
    y = center[1] + radius * np.outer(np.sin(u), np.sin(v))
    z = center[2] + radius * np.outer(np.ones_like(u), np.cos(v))

    ax.plot_surface(x, y, z, color=color, alpha=alpha, linewidth=0)

# parameters for sphere packing
N_x = 5      # Anzahl Kugeln in x-Richtung
N_y = 5      # Anzahl Kugeln in y-Richtung

# Wir setzen den Kugeldurchmesser = 1 => Pitch = 1
# Dann ist der Radius = 0.5
pitch = 1.0
radius = 0.5

# Vertikaler Abstand zwischen aufeinanderliegenden Schichten
z_offset = np.sqrt(6)/3 * pitch  # ~ 0.8165 bei pitch=1

# Listen für Kugelzentren
positions_A1 = []  # erste (untere) A-Lage
positions_B = []   # mittlere B-Lage
positions_A2 = []  # obere A-Lage

# 1) Schicht A (unten, z=0)
for j in range(N_y):
    for i in range(N_x):
        xA = (i + 0.5*(j % 2)) * pitch
        yA = (np.sqrt(3)/2) * j * pitch
        zA = 0.0
        positions_A1.append((xA, yA, zA))

# 2) Schicht B (mittig, z=z_offset)
# => Lateral zusätzlich um (0.5, sqrt(3)/6)
for j in range(N_y):
    for i in range(N_x):
        xB = (i + 0.5*(j % 2)) * pitch + 0.5*pitch
        yB = (np.sqrt(3)/2) * j * pitch + (np.sqrt(3)/6)*pitch
        zB = z_offset
        positions_B.append((xB, yB, zB))

# 3) Schicht A (oben, z=2*z_offset)
#    => Gleiche (x,y) wie A1, aber z=2*z_offset
for j in range(N_y):
    for i in range(N_x):
        xA2 = (i + 0.5*(j % 2)) * pitch
        yA2 = (np.sqrt(3)/2) * j * pitch
        zA2 = 2.0 * z_offset
        positions_A2.append((xA2, yA2, zA2))

# Alles in einer Liste sammeln (nur der Übersicht halber)

all_positions = (positions_A1 + positions_B + positions_A2)


# Plotten
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Untere A-Lage (blau)
for pos in positions_A1:
    plot_sphere(ax, pos, radius=radius, color='cornflowerblue', alpha=0.6)

# Mittlere B-Lage (orange)
for pos in positions_B:
    plot_sphere(ax, pos, radius=radius, color='darkorange', alpha=0.6)

# Obere A-Lage (grün)
for pos in positions_A2:
    plot_sphere(ax, pos, radius=radius, color='green', alpha=0.6)

# Achsen hübsch setzen, damit nichts verzerrt
all_positions_arr = np.array(all_positions)
x_vals = all_positions_arr[:,0]
y_vals = all_positions_arr[:,1]
z_vals = all_positions_arr[:,2]

# Grenzen bestimmen
max_range = np.array([
    x_vals.max()-x_vals.min(),
    y_vals.max()-y_vals.min(),
    z_vals.max()-z_vals.min()
]).max()

mid_x = (x_vals.max()+x_vals.min()) * 0.5
mid_y = (y_vals.max()+y_vals.min()) * 0.5
mid_z = (z_vals.max()+z_vals.min()) * 0.5

ax.set_xlim(mid_x - max_range/2, mid_x + max_range/2)
ax.set_ylim(mid_y - max_range/2, mid_y + max_range/2)
ax.set_zlim(mid_z - max_range/2, mid_z + max_range/2)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Dreischichtige (ABA) Kugelpackung')

try:
    ax.set_box_aspect([1, 1, 1])  # macht die Achsen isotrop => Kugeln wirken rund
except:
    pass  # ältere matplotlib-Versionen ignorieren das

plt.tight_layout()
plt.show()