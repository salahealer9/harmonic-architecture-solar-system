import matplotlib.pyplot as plt
import numpy as np

# --- Figure setup ---
fig, ax = plt.subplots(figsize=(6, 6))

# --- FIXED: Expanded visual limits to accommodate Jupiter ---
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(-6.5, 6.5)  # Expanded from -3.5,6 to -6.5,6.5
ax.set_ylim(-6.5, 6.5)  # Expanded from -3.5,6 to -6.5,6.5

# --- Draw the 2.14 AU Harmonic Node ---
circle_harmonia = plt.Circle((0, 0), 2.14, fill=False, color='#2B2F8A',
                             linewidth=2.2, linestyle='--',
                             label='2.14 AU Harmonic Node (Harmonia)')
ax.add_patch(circle_harmonia)

# --- Planetary orbits (approximate circular) ---
planets = {
    'Mars (1.52 AU)': 1.52,
    'Asteroid Belt (inner edge)': 2.20,
    'Asteroid Belt (outer edge)': 3.20,
    'Jupiter (5.20 AU)': 5.20
}

colors = {
    'Mars (1.52 AU)': 'red',
    'Asteroid Belt (inner edge)': '#7A5C41',
    'Asteroid Belt (outer edge)': '#7A5C41',
    'Jupiter (5.20 AU)': '#D4AF37'
}

for name, distance in planets.items():
    orbit = plt.Circle((0, 0), distance, fill=False,
                       color=colors[name], linewidth=2,
                       linestyle='-' if 'Belt' not in name else ':',
                       alpha=0.8, label=name)
    ax.add_patch(orbit)


# --- ADD ASTEROID FIELD VISUALIZATION ---
# Generate random asteroid positions within the belt region
np.random.seed(42)  # For reproducible random dots
n_asteroids = 150   # Number of dots to represent asteroids

# Create asteroids in a donut shape between 2.2 AU and 3.2 AU
inner_radius = 2.2
outer_radius = 3.2

# Generate random points in polar coordinates
angles = np.random.uniform(0, 2*np.pi, n_asteroids)
radii = np.random.uniform(inner_radius, outer_radius, n_asteroids)

# Convert to Cartesian coordinates
x_asteroids = radii * np.cos(angles)
y_asteroids = radii * np.sin(angles)

# Plot the asteroid field with varying sizes and transparency
ax.scatter(x_asteroids, y_asteroids, s=0.8, color='#8B7355', alpha=0.6, 
           label='Asteroid Field')

# Add a few "major asteroid" markers
major_asteroids = {
    'Ceres': 2.77,
    'Vesta': 2.36,
    'Pallas': 2.77
}

for name, distance in major_asteroids.items():
    angle = np.random.uniform(0, 2*np.pi)
    x = distance * np.cos(angle)
    y = distance * np.sin(angle)
    ax.plot(x, y, 'o', markersize=3, color='#5D4037')
    ax.annotate(name, (x, y), xytext=(5, 5), textcoords='offset points', 
                fontsize=7, color='#5D4037')

# --- Add the Sun ---
ax.plot(0, 0, 'yo', markersize=12)
ax.plot(0, 0, 'y*', markersize=22, label='Sun')

# --- Annotations ---
ax.annotate('2.14 AU\nHarmonic Node',
            xy=(1.45, 1.45), xytext=(2.6, 3),
            arrowprops=dict(arrowstyle='->', color='#2B2F8A', lw=1.3),
            fontsize=10.5, color='#2B2F8A', ha='center', va='center')

# --- Labels and title ---
ax.set_xlabel('Distance (AU)', fontsize=11)
ax.set_ylabel('Distance (AU)', fontsize=11)
ax.set_title('Solar System Geometry: The 2.14 AU Harmonic Node (Harmonia)', fontsize=12.5)

# --- Legend and grid ---
ax.legend(loc='upper left', fontsize=8.5, frameon=True)
ax.grid(True, alpha=0.25)

# --- Style and output ---
fig.patch.set_facecolor('#fafafa')
plt.tight_layout()
plt.savefig("harmonia_orbit_node_2_14.pdf", dpi=300, bbox_inches='tight')
plt.show()