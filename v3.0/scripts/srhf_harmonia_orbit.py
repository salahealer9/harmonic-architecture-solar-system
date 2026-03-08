# =====================================================
# SRHF Harmonic Model – Harmonia Node Orbit Schematic
# Schematic view of the 2.14 AU SRHF harmonic node (Harmonia)
# Output: srhf_harmonia_orbit.png (Figure 2)
# =====================================================

import matplotlib.pyplot as plt
import numpy as np

# --- Figure & style setup ---
fig, ax = plt.subplots(figsize=(6, 6))

bg = "#f8f8f8"
grid_color = "#e0e0e0"

ax.set_aspect("equal", adjustable="box")
ax.set_xlim(-6.5, 6.5)
ax.set_ylim(-6.5, 6.5)
ax.set_facecolor(bg)
fig.patch.set_facecolor(bg)
ax.set_axisbelow(True)
ax.grid(True, color=grid_color, linewidth=1.0, alpha=0.8)

# --- Draw the 2.14 AU SRHF Harmonic Node ---
circle_harmonia = plt.Circle(
    (0, 0),
    2.14,
    fill=False,
    color="#2B2F8A",
    linewidth=2.2,
    linestyle="--",
    label="2.14 AU SRHF harmonic node (Harmonia)",
)
ax.add_patch(circle_harmonia)

# --- Planetary orbits (approximate circular) ---
planets = {
    "Mars (1.52 AU)": 1.52,
    "Asteroid belt (inner edge)": 2.20,
    "Asteroid belt (outer edge)": 3.20,
    "Jupiter (5.20 AU)": 5.20,
}

colors = {
    "Mars (1.52 AU)": "red",
    "Asteroid belt (inner edge)": "#7A5C41",
    "Asteroid belt (outer edge)": "#7A5C41",
    "Jupiter (5.20 AU)": "#D4AF37",
}

for name, distance in planets.items():
    orbit = plt.Circle(
        (0, 0),
        distance,
        fill=False,
        color=colors[name],
        linewidth=2,
        linestyle="-" if "belt" not in name else ":",
        alpha=0.85,
        label=name,
    )
    ax.add_patch(orbit)

# --- Asteroid field visualization (inner main belt) ---
np.random.seed(42)         # reproducible random dots
n_asteroids = 150

inner_radius = 2.2
outer_radius = 3.2

angles = np.random.uniform(0, 2 * np.pi, n_asteroids)
radii = np.random.uniform(inner_radius, outer_radius, n_asteroids)

x_asteroids = radii * np.cos(angles)
y_asteroids = radii * np.sin(angles)

ax.scatter(
    x_asteroids,
    y_asteroids,
    s=0.8,
    color="#8B7355",
    alpha=0.6,
    label="Asteroid belt (schematic)"
)

# --- Major asteroid markers (schematic positions) ---
major_asteroids = {
    "Ceres": 2.77,
    "Vesta": 2.36,
    "Pallas": 2.77,
}

for name, distance in major_asteroids.items():
    angle = np.random.uniform(0, 2 * np.pi)
    x = distance * np.cos(angle)
    y = distance * np.sin(angle)
    ax.plot(x, y, "o", markersize=3, color="#5D4037")
    ax.annotate(
        name,
        (x, y),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=7,
        color="#5D4037",
    )

# --- Sun at the centre ---
ax.plot(0, 0, "yo", markersize=12)
ax.plot(0, 0, "y*", markersize=22, label="Sun")

# --- Annotation for Harmonia node ---
ax.annotate(
    "2.14 AU\nSRHF harmonic node",
    xy=(1.45, 1.45),
    xytext=(2.7, 3.1),
    arrowprops=dict(arrowstyle="->", color="#2B2F8A", lw=1.3),
    fontsize=10.5,
    color="#2B2F8A",
    ha="center",
    va="center",
)

# --- Labels and title ---
ax.set_xlabel("Distance (AU)", fontsize=11)
ax.set_ylabel("Distance (AU)", fontsize=11)
ax.set_title(
    "Inner Solar System Geometry:\nSRHF Harmonic Node at 2.14 AU (Harmonia)",
    fontsize=12.5,
)

# --- Legend ---
# Matplotlib will duplicate labels for multiple patches; this cleans them up.
handles, labels = ax.get_legend_handles_labels()
unique = dict(zip(labels, handles))
ax.legend(
    unique.values(),
    unique.keys(),
    loc="upper left",
    fontsize=8.0,
    frameon=True,
)

plt.tight_layout()
plt.savefig("srhf_harmonia_orbit.png", dpi=300, bbox_inches="tight", facecolor=bg)
plt.show()
