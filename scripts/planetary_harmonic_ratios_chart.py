import matplotlib.pyplot as plt
import numpy as np

# ================================
# Planetary Harmonic Ratios Chart
# ================================

# Planet names (order of model progression)
planets = [
    "Mercury", "Venus", "Earth", "Mars", 
    "Harmonia", "Jupiter", "Saturn", 
    "Uranus", "Neptune", "Pluto"
]

# Observed orbital distances (in AU)
observed = np.array([0.387, 0.723, 1.000, 1.524, np.nan, 5.204, 9.582, 19.201, 30.047, 39.482])

# Predicted harmonic distances (based on Celtic Cross constants)
predicted = np.array([0.385, 0.707, 1.000, 1.519, 2.145, 5.196, 9.555, 19.155, 30.032, 39.450])

# Set up figure
plt.figure(figsize=(10, 6))
plt.title("Comparative Harmonic Ratios of Planetary Distances", fontsize=14, weight='bold')

# Plot predicted harmonic model
plt.plot(planets, predicted, '-o', color="#5a58a2", label='Predicted (Celtic Cross Model)', linewidth=2.2, markersize=7)

# Plot observed data (excluding Harmonia)
mask = ~np.isnan(observed)
plt.plot(np.array(planets)[mask], observed[mask], '-o', color="#e09b3d", label='Observed (Empirical)', linewidth=2.2, markersize=7)

# Highlight Harmonia
plt.scatter("Harmonia", predicted[4], color="#c53a38", s=90, zorder=5, label="Predicted Harmonia")

# Aesthetic adjustments
plt.grid(alpha=0.25)
plt.ylabel("Orbital Distance (AU)", fontsize=12)
plt.xticks(rotation=30, ha='right')
plt.legend(frameon=False, loc="upper left", fontsize=10)
plt.tight_layout()

# Export to PDF
plt.savefig("planetary_harmonic_ratios_chart.pdf", bbox_inches='tight')
plt.show()
