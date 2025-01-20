import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 1) Kugel-Plot-Funktion
def plot_sphere(ax, center, radius=0.4, color='C0', alpha=1.0, resolution=12):
    u = np.linspace(0, 2*np.pi, resolution)
    v = np.linspace(0, np.pi, resolution)
    
    x = center[0] + radius * np.outer(np.cos(u), np.sin(v))
    y = center[1] + radius * np.outer(np.sin(u), np.sin(v))
    z = center[2] + radius * np.outer(np.ones_like(u), np.cos(v))
    ax.plot_surface(x, y, z, color=color, alpha=alpha, linewidth=0)


# 2) Dreiecksschicht (oben/unten): 6 Kugeln in 1-2-3
def triangular_6_layer(z, pitch=0.8):
    coords = []
    rowSpacing = (np.sqrt(3)/2)*pitch
    for j in range(3):  # j=0..2 => 1,2,3 Kugeln
        yj = j*rowSpacing
        xLeft = -(j*pitch)/2.0
        for i in range(j+1):
            xij = xLeft + i*pitch
            coords.append((xij, yj, z))
    return coords


# 3) Hexagon + Zentralkugel in mittlerer Ebene
def circle_points_z(z, r, n=6, offset_deg=0.0):
    coords = []
    offset_rad = np.radians(offset_deg)
    for k in range(n):
        angle = 2*np.pi*k/n + offset_rad
        x = r*np.cos(angle)
        y = r*np.sin(angle)
        coords.append((x, y, z))
    return coords


# 4) Parameter
pitch = 0.8      
sphere_rad = 0.4 
z_offset = 0.8   


# 5) Schichten: A-B-A
z_top = +z_offset
z_mid = 0.0
z_bot = -z_offset

positions_A_top = triangular_6_layer(z=z_top, pitch=pitch)

hex_radius = 0.8
positions_B_mid_hex = circle_points_z(z_mid, r=hex_radius, n=6, offset_deg=0.0)

# Y-Verschiebung (z.B. +0.4)
shifted_hex = []
for (x, y, z) in positions_B_mid_hex:
    shifted_hex.append((x, y + 0.4, z))

center_B = (0, 0.4, z_mid)  # Zentralkugel

positions_B_mid = shifted_hex + [center_B]

positions_A_bot = triangular_6_layer(z=z_bot, pitch=pitch)


# 6) Plot
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# (A) Obere Schicht (A) => T0..T5
for i, pos in enumerate(positions_A_top):
    plot_sphere(ax, pos, sphere_rad, color='cornflowerblue', alpha=0.4)
    ax.text(pos[0]+0.05, pos[1]+0.05, pos[2]+0.05, f"T{i}", fontsize=12, color='black')

# (B) Mittlere Schicht (B) => M0..M5 (Ring), M6 (Zentralkugel)
for i, pos in enumerate(shifted_hex):
    plot_sphere(ax, pos, sphere_rad, color='darkorange', alpha=0.4)
    ax.text(pos[0]+0.05, pos[1]+0.05, pos[2]+0.05, f"M{i}", fontsize=12, color='black')

plot_sphere(ax, center_B, sphere_rad, color='red', alpha=0.4)
ax.text(center_B[0]+0.05, center_B[1]+0.05, center_B[2]+0.05, "M6", fontsize=12, color='black')

# (C) Untere Schicht (A, grün) => ohne Beschriftung
for pos in positions_A_bot:
    plot_sphere(ax, pos, sphere_rad, color='seagreen', alpha=0.4)

# 7) Oktaeder nach Vorgabe
# Oberes Dreieck: T4, T1, T2
# "Unteres" Dreieck (B): M1, M2, M6
# Zusätzliche Kanten:
#   T4->(M1,M2),  M6->(T1,T2)
# + NEU: T2->M1 und T1->M2

# Schauen wir in die Indizes:
# T4 = positions_A_top[4]
# T1 = positions_A_top[1]
# T2 = positions_A_top[2]
# M1 = shifted_hex[1]
# M2 = shifted_hex[2]
# M6 = center_B

T4 = positions_A_top[4]  # Oberes
T1 = positions_A_top[1]
T2 = positions_A_top[2]

M1 = shifted_hex[1]      # Mittlere
M2 = shifted_hex[2]
M6 = center_B

# => Array: [T4, T1, T2, M1, M2, M6]
# Indizes:   0    1    2    3    4    5
oct_points = np.array([T4, T1, T2, M1, M2, M6])
labels_okt = ["T4","T1","T2","M1","M2","M6"]

edges = set()
# Oberes Dreieck: T4->T1->T2 => (0->1->2->0)
edges.update([(0,1),(1,2),(2,0)])

# Unteres Dreieck (in B): M1->M2->M6 => (3->4->5->3)
edges.update([(3,4),(4,5),(5,3)])

# Zusätzliche Kanten:
# T4->(M1,M2) => (0->3), (0->4)
edges.update([(0,3),(0,4)])
# M6->(T1,T2) => (5->1),(5->2)
edges.update([(5,1),(5,2)])
# NEU:
# T2->M1 => (2->3)
# T1->M2 => (1->4)
edges.update([(2,3),(1,4)])

# Doppelte entfernen
final_edges = []
for (i1,i2) in edges:
    i_min, i_max = min(i1,i2), max(i1,i2)
    final_edges.append((i_min,i_max))
final_edges = list(set(final_edges))

# Zeichnen
for (i1,i2) in final_edges:
    p1 = oct_points[i1]
    p2 = oct_points[i2]
    ax.plot([p1[0], p2[0]],
            [p1[1], p2[1]],
            [p1[2], p2[2]],
            color='k', linewidth=4, alpha = 1.0)

# Beschriftung der 6 Eckpunkte
for i,(x,y,z) in enumerate(oct_points):
    ax.text(x+0.07, y+0.07, z+0.07, labels_okt[i], fontsize=12, color='magenta')

# 8) Achsenlimits (mit mehr Rand)
all_positions = (positions_A_top + shifted_hex + [center_B] + positions_A_bot)
all_positions_arr = np.array(all_positions)

x_vals = all_positions_arr[:,0]
y_vals = all_positions_arr[:,1]
z_vals = all_positions_arr[:,2]

max_range = np.array([
    x_vals.max()-x_vals.min(),
    y_vals.max()-y_vals.min(),
    z_vals.max()-z_vals.min()
]).max()

mid_x = 0.5*(x_vals.max()+x_vals.min())
mid_y = 0.5*(y_vals.max()+y_vals.min())
mid_z = 0.5*(z_vals.max()+z_vals.min())

axis_padding = 1.2
ax.set_xlim(mid_x - (max_range*axis_padding/2),
            mid_x + (max_range*axis_padding/2))
ax.set_ylim(mid_y - (max_range*axis_padding/2),
            mid_y + (max_range*axis_padding/2))
ax.set_zlim(mid_z - (max_range*axis_padding/2),
            mid_z + (max_range*axis_padding/2))

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('Oktaederlücke in hexagonal dichtester Kugelpackung')

try:
    ax.set_box_aspect([1, 1, 1])  # macht die Achsen isotrop => Kugeln wirken rund
except:
    pass  # ältere matplotlib-Versionen ignorieren das

plt.tight_layout()
plt.show()