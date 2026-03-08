# =====================================================
# SRHF Harmonic Model – Full-System Distances
# Output: srhf_ratios_full.png (Figure 6a)
# =====================================================

import matplotlib.pyplot as plt
import numpy as np

# Planet names (including Harmonia)
planets = [
    "Mercury", "Venus", "Earth", "Mars",
    "Harmonia", "Jupiter", "Saturn",
    "Uranus", "Neptune", "Pluto"
]

# Observed semi-major axes (AU)
# Consistent with JPL Horizons values used in the paper
observed = np.array([
    0.387,   # Mercury
    0.722,   # Venus
    1.000,   # Earth
    1.524,   # Mars
    np.nan,  # Harmonia (hypothesised, no observed value)
    5.204,   # Jupiter
    9.559,   # Saturn
    19.185,  # Uranus
    30.156,  # Neptune
    39.482   # Pluto
])

# Predicted semi-major axes (AU) from the SRHF harmonic model
# Consistent with Table 1 in the manuscript
predicted = np.array([
    0.387,   # Mercury
    0.707,   # Venus
    1.000,   # Earth
    1.547,   # Mars
    2.142,   # Harmonia (SRHF harmonic node)
    5.172,   # Jupiter
    9.456,   # Saturn
    18.912,  # Uranus
    30.142,  # Neptune
    39.598   # Pluto
])

# =====================================================
# Colours (SRHF palette)
# =====================================================
indigo = "#2B2F8A"
srhf_algebraic_color = "#E07A1A"
robin_egg_blue = "#1FCECB"     # real/empirical data for observed planets

# --- Plot setup ---
fig, ax = plt.subplots(figsize=(10, 6))

# Background color
bg = "#f8f8f8"
ax.set_facecolor(bg)
fig.patch.set_facecolor(bg)

ax.set_axisbelow(True)
ax.grid(
    True,
    color="#e0e0e0",
    linewidth=1.0,
    alpha=0.85
)

ax.set_title("SRHF Harmonic Model: Observed vs Predicted Planetary Distances",
          fontsize=14, weight='bold')

# SRHF predicted sequence (indigo-like)
ax.plot( 
    planets,
    predicted,
    '-o',
    color=indigo,
    label="Predicted (SRHF harmonic model)",
    linewidth=2.2,
    markersize=7,
)

# Observed data (exclude Harmonia where observed is NaN)
mask_obs = ~np.isnan(observed)
ax.plot(
    np.array(planets)[mask_obs],
    observed[mask_obs],
    '-o',
    color=robin_egg_blue,
    label="Observed (JPL Horizons)",
    linewidth=2.2,
    markersize=7,
)

# Highlight Harmonia prediction explicitly
ax.scatter(
    "Harmonia",
    predicted[4],
    color=srhf_algebraic_color,
    s=90,
    zorder=5,
    label="SRHF Harmonia node"
)

ax.set_ylabel("Semi-major axis (AU)", fontsize=12) 

ax.set_xticks(range(len(planets))) 
ax.set_xticklabels(planets, rotation=30, ha='right')

ax.legend(frameon=False, loc="upper left", fontsize=10)

plt.tight_layout()

# Export PNG (high resolution)
plt.savefig("srhf_ratios_full.png", dpi=300, bbox_inches='tight', facecolor=bg)
plt.show()