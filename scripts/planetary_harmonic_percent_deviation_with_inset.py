import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from matplotlib.patches import ConnectionPatch

# --- Constants (Celtic Cross ratios) ---
A = np.sqrt(2)
B = A + 1
C = 2*A - 1
D = A - 1
H = 2.1437 

# --- Observed semi-major axes (AU) ---
planets = ["Mercury", "Venus", "Earth", "Mars",
           "Harmonia", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

a_obs = np.array([0.387, 0.722, 1.000, 1.524,
                  H, 5.204, 9.559, 19.185, 30.156, 39.482])

# --- Celtic model predictions (AU) ---
a_celtic = np.array([
    (14/15)*D,       # Mercury
    1/A,             # Venus
    1.0,             # Earth
    (B+D)/C,         # Mars
    (2*A*C)/(1+A),   # Harmonia
    2*A*C,           # Jupiter
    2*A*C**2,        # Saturn
    4*A*C**2,        # Uranus
    2*A*C*(B/D),     # Neptune
    4*A*C*(A+B)      # Pluto
])

# --- Calculate % deviations ---
deviation = (a_celtic / a_obs - 1) * 100

# --- Harmonia variants ---
lp_empirical = 2.1437  # This is our REFERENCE for the inset
lp_pi = np.pi**(2/3)
lp_celtic = (2*A*C)/(1+A)
lp_index = planets.index("Harmonia")

# --- Colors (gold–indigo palette) ---
gold = "#D4AF37"
indigo = "#2B2F8A"
teal = "#1F7A8C"
gray = "#4D4D4D"

# --- Plot setup ---
fig, ax = plt.subplots(figsize=(12, 7))
x_positions = np.arange(len(planets))
ax.plot(x_positions, deviation, 'o-', color=indigo, lw=2.2, markersize=6, label="Celtic Cross model")

# Add shaded ±0.72% MAPE band
ax.fill_between(x_positions, -0.72, 0.72, color='gray', alpha=0.15, label='±0.72% global precision')

# Mark Harmonia variants - using observed position as reference
ax.scatter(lp_index, (lp_celtic/H-1)*100, color=gold, s=90, edgecolor='black', label="Celtic prediction")
ax.scatter(lp_index, (lp_empirical/H-1)*100, color=indigo, s=90, edgecolor='black', label="Empirical optimum")
ax.scatter(lp_index, (lp_pi/H-1)*100, color=teal, s=90, edgecolor='black', label=r"$\pi^{2/3}$ attractor")

# Reference lines
ax.axhline(0, color=gray, linestyle='--', lw=1)
ax.axhline(2, color=gray, linestyle=':', lw=0.8, alpha=0.5)
ax.axhline(-2, color=gray, linestyle=':', lw=0.8, alpha=0.5)

# Labels and styling
ax.set_ylabel("Deviation from Observed Distance (%)", fontsize=12)
ax.set_xlabel("Planet", fontsize=12)
ax.set_title("Percentage Deviation of Celtic Harmonic Model from Observed Planetary Distances", fontsize=14)
ax.set_xticks(x_positions)
ax.set_xticklabels(planets, rotation=35)
ax.set_ylim(-2.5, 2.5)
ax.legend(fontsize=9, loc="upper right", frameon=True)
ax.grid(alpha=0.3)

# --- ADD INSET ZOOM PLOT ---
ax_inset = inset_axes(ax, width="20%", height="20%", loc='lower center',
                     bbox_to_anchor=(-0.07, 0.1, 1, 1), bbox_transform=ax.transAxes)

# Focus on Harmonia region
focus_planets = ["Mars", "Harmonia", "Jupiter"]
focus_indices = [3, 4, 5]
focus_positions = [0, 1, 2]

# Plot the same data but zoomed in
ax_inset.plot(focus_positions, [deviation[i] for i in focus_indices], 
              'o-', color=indigo, lw=2, markersize=6)

# CRITICAL CHANGE: Calculate percentages relative to EMPIRICAL OPTIMUM (2.1437 AU)
ax_inset.scatter(1, (lp_celtic/lp_empirical-1)*100, color=gold, s=80, edgecolor='black', zorder=5)
ax_inset.scatter(1, 0, color=indigo, s=80, edgecolor='black', zorder=5)  # Empirical is our zero reference
ax_inset.scatter(1, (lp_pi/lp_empirical-1)*100, color=teal, s=80, edgecolor='black', zorder=5)

# Inset styling
ax_inset.axhline(0, color=gray, linestyle='--', lw=0.8, alpha=0.7)
ax_inset.set_ylim(-0.15, 0.15)  # Adjusted for the 0.07% range
ax_inset.set_title("Deviation from Empirical Optimum", fontsize=9, pad=3)  # Updated title
ax_inset.grid(True, alpha=0.4)
ax_inset.tick_params(axis='both', which='major', labelsize=7)
ax_inset.set_xticks(focus_positions)
ax_inset.set_xticklabels(focus_planets, rotation=35, fontsize=7)

# Updated text annotations - relative to empirical optimum
ax_inset.text(1.1, (lp_celtic/lp_empirical-1)*100, f'{(lp_celtic/lp_empirical-1)*100:.3f}%', 
              fontsize=6, va='center')
ax_inset.text(1.1, 0, f'0.000%', fontsize=6, va='center')  # Empirical is reference
ax_inset.text(1.1, (lp_pi/lp_empirical-1)*100, f'{(lp_pi/lp_empirical-1)*100:.3f}%', 
              fontsize=6, va='center')

from matplotlib.patches import ConnectionPatch

# Subtle, properly scaled arrow
con = ConnectionPatch(
    xyA=(lp_index, -0.25),           # Start from above Harmonia points
    xyB=(0.45, 1.2),               # Point to top-center of inset
    coordsA="data", coordsB="axes fraction", 
    axesA=ax, axesB=ax_inset,
    color="#FF6B6B", linewidth=1.5, alpha=0.6,  # More subtle
    arrowstyle="->,head_width=0.5,head_length=1"  # Smaller head
)
ax.add_artist(con)

# Optional subtle label
ax.text(lp_index- 0.4, -0.48, "zoom", ha='center', va='bottom', 
        fontsize=8, color='gray', alpha=0.7)

plt.savefig("planetary_harmonic_percent_deviation_with_inset.pdf", dpi=300, bbox_inches='tight')
plt.show()