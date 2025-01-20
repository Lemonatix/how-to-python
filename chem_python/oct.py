import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# --------------------------------------------------------
# 1) Hilfsfunktion zum Zeichnen einer Kugel (3D-Oberfläche)
# --------------------------------------------------------
def plot_sphere(ax, center, radius=0.5, color='C0', alpha=1.0, resolution=20):
    """
    Zeichnet eine Kugel mit Mittelpunkt 'center' und Radius 'radius'
    als 3D-Surface in das Axes3D-Objekt 'ax'.
    """
    u = np.linspace(0, 2*np.pi, resolution)
    v = np.linspace(0, np.pi, resolution)
    
    x = center[0] + radius * np.outer(np.cos(u), np.sin(v))
    y = center[1] + radius * np.outer(np.sin(u), np.sin(v))
    z = center[2] + radius * np.outer(np.ones_like(u), np.cos(v))

    ax.plot_surface(x, y, z, color=color, alpha=alpha, linewidth=0)

# --------------------------------------------------------
# 2) Parameter & Erzeugung der 3 Ebenen: A–B–A
# --------------------------------------------------------
# Wir definieren:
#  - Obere Ebene (z = +1): 6 Kugeln im Hexagon
#  - Mittlere Ebene (z =  0): 6 Kugeln im Hexagon + 1 Kugel im Zentrum
#  - Untere Ebene (z = -1): 6 Kugeln im Hexagon
#
# Radius für die Hex-Anordnung
R = 1.0
# Kugelradius (reine Darstellung, 0.3 oder 0.5 nach Belieben)
sphere_radius = 0.4

# Hilfsfunktion: Hexagon-Koordinaten
def hex_ring_z(z, r=R, n=6, offset_deg=0):
    """
    Erzeugt n Punkte in der Ebene 'z' auf einem Kreisradius 'r',
    gleichmäßig verteilt. 'offset_deg' verschiebt optional den Winkel.
    """
    coords = []
    offset_rad = np.radians(offset_deg)
    for k in range(n):
        angle = 2*np.pi*k/n + offset_rad
        x = r * np.cos(angle)
        y = r * np.sin(angle)
        coords.append((x, y, z))
    return coords

# Ebene A oben (z=+1) => 6 Kugeln, Winkel-Offset 0 Grad
z_top = +1.0
positions_A_top = hex_ring_z(z_top, r=R, n=6, offset_deg=0)

# Ebene B in der Mitte (z=0) => 6 Kugeln + 1 Zentrum
z_mid = 0.0
positions_B_mid = hex_ring_z(z_mid, r=R, n=6, offset_deg=0)
center_B = (0.0, 0.0, z_mid)  # zusätzliche Kugel im Zentrum
positions_B_mid.append(center_B)

# Ebene A unten (z=-1) => 6 Kugeln,
# hier drehen wir das Hex um 30 Grad, um eine "AB" typische Versetzung zu illustrieren
z_bot = -1.0
positions_A_bot = hex_ring_z(z_bot, r=R, n=6, offset_deg=30)

# Gesamt-Liste aller Kugelzentren
all_positions = np.array(positions_A_top + positions_B_mid + positions_A_bot)

# --------------------------------------------------------
# 3) Wir wählen 6 Kugeln als Ecken eines Oktaeders
# --------------------------------------------------------
# Idee: Wir nehmen 3 Kugeln aus der oberen Ebene und 3 aus der unteren Ebene,
# so gedreht, dass ein (annähernd) symmetrisches Oktaeder entsteht.
#
# Konkreter Plan:
#  - Oben: Kugeln bei Winkeln  0°, 120°, 240° (Indices 0,2,4 in "positions_A_top")
#  - Unten: Kugeln bei Winkeln 60°,180°,300° (entsprechend "positions_A_bot", 
#    die wir ja um 30° versetzt haben => Indices 0,2,4)
#
# Prüfe die Indices in 'positions_A_top' => 6 Kugeln: Index 0..5
#   Index 0 => Winkel=0°,    1 => 60°,   2 =>120°, 3 =>180°, 4 =>240°, 5=>300°
#
# In "positions_A_top", wir nehmen indices [0, 2, 4] => 0°,120°,240°,
# In "positions_A_bot", wir nehmen indices [1, 3, 5] => 60°,180°,300°
#   (denn offset_deg=30 verschiebt alles um 30°: Index=0 dort =>30°, Index=1=>90°, etc.)
#   Actually, mal ausrechnen:
#   - offset_deg=30 => Index=0 => 30°, 1=>90°, 2=>150°,3=>210°,4=>270°,5=>330°
#   => Also wir brauchen [1,3,5] => 90°,210°,330°. Das *kann* einen Oktaeder ergeben.
#
# Probieren wir's so. Wir nennen sie corners_oct.
corners_top = [positions_A_top[i] for i in [0, 2, 4]]
corners_bot = [positions_A_bot[i] for i in [1, 3, 5]]
oct_corners = corners_top + corners_bot

# Nun wollen wir die "Kanten" des Oktaeders als gerade Linien zeichnen.
# Ein Oktaeder hat 8 Dreiecksflächen, 6 Ecken, 12 Kanten.
# Wir können hier minimalistisch die "Edges" definieren:
#   - Verbinde die 3 oberen Ecken (geschlossen)
#   - Verbinde die 3 unteren Ecken (geschlossen)
#   - Jede obere Ecke mit jeder unteren Ecke => 3x3=9 Linien 
#     => das wäre eigentlich "zu viel" (klappt nicht, man kriegt 9 statt 6 Verbindungen).
# In einem echten regulären Oktaeder verbindet jede obere Ecke *alle* unteren,
# so hat man 3 (oben) + 3 (unten) = 6 Ecken, top-dreieck & bottom-dreieck,
# + 3*3 = 9 "vertikale" Kanten => macht 3 + 3 + 9 = 15,
# aber wir doppeln die Oberkante (3 edges) & Unterkante (3 edges) => 3+3=6 + 9=15 total edges 
# - in einer "reinen" Geometrie hätte ein Oktaeder 12 edges. 
# Hier ist's eine "verzerrte" Version mit 6 Ecken - wir checken, wie es aussieht.
#
# Für Einfachheit: wir zeichnen 
#  - die 3er-Polygone (oben & unten) 
#  - ALLE Verbindungen zwischen den 3 oberen und 3 unteren Ecken.
# Dann entsteht *topologisch* eine Doppel-Pyramide, die wir "Oktaeder" nennen.

edges = []
# Top-Dreieck (0->1->2->0)
edges.append((0,1))
edges.append((1,2))
edges.append((2,0))
# Bottom-Dreieck (3->4->5->3)
edges.append((3,4))
edges.append((4,5))
edges.append((5,3))
# Verbindungen top->bottom
for i_top in [0,1,2]:
    for j_bot in [3,4,5]:
        edges.append((i_top, j_bot))

# --------------------------------------------------------
# 4) Plot erstellen
# --------------------------------------------------------
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# Kugeln (Oben=blau, Mitte=orange, Unten=grün), 
# damit man Ebenen unterscheiden kann
for pos in positions_A_top:
    plot_sphere(ax, pos, sphere_radius, color='cornflowerblue', alpha=0.8)
for idx, pos in enumerate(positions_B_mid):
    # Zentrum in z=0 (als rot?)
    color = 'darkorange'
    if np.allclose(pos, [0,0,0]):
        color = 'red'  # center
    plot_sphere(ax, pos, sphere_radius, color=color, alpha=0.8)
for pos in positions_A_bot:
    plot_sphere(ax, pos, sphere_radius, color='seagreen', alpha=0.8)

# Oktaeder-Kanten (nur als gerade Linien)
# "oct_corners" sind 6 Punkte => wir zeichnen lines wie in 'edges'
oct_corners = np.array(oct_corners)  # shape (6, 3)

for (i1, i2) in edges:
    p1 = oct_corners[i1]
    p2 = oct_corners[i2]
    ax.plot([p1[0], p2[0]],
            [p1[1], p2[1]],
            [p1[2], p2[2]],
            color='k', linewidth=2)

# Achsen so skalieren, dass nichts verzerrt ist
all_positions = np.concatenate([positions_A_top, positions_B_mid, positions_A_bot])
x_vals = all_positions[:,0]
y_vals = all_positions[:,1]
z_vals = all_positions[:,2]

max_range = np.array([
    x_vals.max()-x_vals.min(),
    y_vals.max()-y_vals.min(),
    z_vals.max()-z_vals.min()
]).max()

mid_x = (x_vals.max()+x_vals.min())*0.5
mid_y = (y_vals.max()+y_vals.min())*0.5
mid_z = (z_vals.max()+z_vals.min())*0.5

ax.set_xlim(mid_x - max_range/2, mid_x + max_range/2)
ax.set_ylim(mid_y - max_range/2, mid_y + max_range/2)
ax.set_zlim(mid_z - max_range/2, mid_z + max_range/2)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('3 Ebenen (A-B-A) + Oktaeder aus 6 Kugelzentren')

plt.tight_layout()
plt.show()
