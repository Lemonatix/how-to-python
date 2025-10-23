import numpy as np
import matplotlib.pyplot as plt

def normal_pdf(x, mu, sigma):
    return np.exp(-(x - mu)**2 / (2 * sigma**2)) / (sigma * np.sqrt(2*np.pi))

x = np.linspace(-8, 8, 1200)
ref = 0.0

# (Titel, Mittelwert μ, Std.-Abw. σ)
cases = [
    ("genau (richtig & präzise)", 0.0, 0.35),
    ("richtig aber unpräzise",   0.0, 1.60),
    ("präzise aber falsch",      2.0, 0.50),
    ("unpräzise und falsch",    -2.0, 1.80),
]

fig, axes = plt.subplots(2, 2, figsize=(10, 7), sharex=True)
axes = axes.ravel()

for i, (ax, (title, mu, sigma)) in enumerate(zip(axes, cases)):
    y = normal_pdf(x, mu, sigma)
    ax.plot(x, y, linewidth=2)                     
    ax.axvline(ref, linestyle="--", linewidth=2)
    ax.set_title(title)
    ax.set_xlim(-8, 8)
    ax.grid(True, alpha=0.3)
    ax.text(0.98, 0.95, rf"$\mu={mu:.1f},\ \sigma={sigma:.2f}$",
            transform=ax.transAxes, ha="right", va="top")

    if i in (0, 2):
        ax.set_ylabel("Häufigkeit / Dichte")
    if i in (2, 3):
        ax.set_xlabel("Messwert")

fig.tight_layout(rect=(0, 0, 1, 0.95))
plt.show()