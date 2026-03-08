# =====================================================
# SRHF Harmonic Model – Percentage Deviations vs Observed
# Log-scale Validation + Harmonia Inset
# Output: srhf_percent_deviation.png (Figure 7a)
# =====================================================

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from matplotlib.patches import ConnectionPatch

# --- Constants (SRHF harmonic ratios) ---
A = np.sqrt(2)
B = A + 1
C = 2*A - 1
D = A - 1
H = 2.1437   # Empirical Harmonia node a_H^{opt}

# --- Observed semi-major axes (AU) ---
planets = [
    "Mercury", "Venus", "Earth", "Mars",
    "Harmonia", "Jupiter", "Saturn",
    "Uranus", "Neptune", "Pluto"
]

a_obs = np.array([
    0.387, 0.722, 1.000, 1.524,
    H, 5.204, 9.559, 19.185, 30.156, 39.482
])

# --- SRHF algebraic model predictions (AU) ---
a_srhf = np.array([
    (14/15)*D,       # Mercury
    1/A,             # Venus
    1.0,             # Earth
    (B + D)/C,       # Mars
    (2*A*C)/(1 + A), # Harmonia (SRHF algebraic prediction)
    2*A*C,           # Jupiter
    2*A*C**2,        # Saturn
    4*A*C**2,        # Uranus
    2*A*C*(B/D),     # Neptune
    4*A*C*(A + B)    # Pluto
])

# --- Calculate % deviations relative to observed ---
deviation = (a_srhf / a_obs - 1) * 100

# --- Harmonia variants ---
lp_empirical = H                   # reference: empirical optimum
lp_pi = np.pi**(2/3)               # SRHF transcendental prediction
lp_srhf = (2*A*C)/(1 + A)          # SRHF algebraic prediction
lp_index = planets.index("Harmonia")

# --- Colors (SRHF palette) ---
srhf_algebraic_color = "#E07A1A"
indigo = "#2B2F8A"
crimson = "#B22222"       # Empirical optimum
teal = "#1F7A8C"
gray = "#4D4D4D"


# --- Main plot setup ---
fig, ax = plt.subplots(figsize=(12, 7))

# Background and grid styling
bg = "#f8f8f8"
grid_color = "#e0e0e0"
ax.set_facecolor(bg)
fig.patch.set_facecolor(bg)
ax.set_axisbelow(True)
ax.grid(True, color=grid_color, linewidth=1.0, alpha=0.85)

x_positions = np.arange(len(planets))

ax.plot(
    x_positions, deviation, 'o-',
    color=indigo, lw=2.2, markersize=6,
    label="SRHF harmonic model"
)

# Shaded ±0.72% MAPE band
ax.fill_between(
    x_positions, -0.72, 0.72,
    color='gray', alpha=0.15,
    label='±0.72% global precision'
)

# Mark Harmonia variants (percent differences relative to observed Harmonia = H)
ax.scatter(lp_index, (lp_srhf/H - 1) * 100,
           color=srhf_algebraic_color, s=90, edgecolor='black',
           label="SRHF algebraic prediction")

ax.scatter(lp_index, (lp_empirical/H - 1) * 100,
           color=crimson, s=90, edgecolor='black',
           label="Empirical optimum")

ax.scatter(lp_index, (lp_pi/H - 1) * 100,
           color=teal, s=90, edgecolor='black',
           label=r"Transcendental prediction $a_H^{\pi}$")

# Reference lines
ax.axhline(0, color=gray, linestyle='--', lw=1)
ax.axhline(2, color=gray, linestyle=':', lw=0.8, alpha=0.5)
ax.axhline(-2, color=gray, linestyle=':', lw=0.8, alpha=0.5)

# Labels and styling
ax.set_ylabel("Deviation from observed distance (%)", fontsize=12)
ax.set_xlabel("Planet", fontsize=12)
ax.set_title(
    "Percentage deviation of SRHF harmonic model\nfrom observed planetary distances",
    fontsize=14
)
ax.set_xticks(x_positions)
ax.set_xticklabels(planets, rotation=35)
ax.set_ylim(-2.5, 2.5)
ax.legend(fontsize=9, loc="upper right", frameon=True)

# --- Inset zoom around Harmonia (relative to empirical optimum) ---
ax_inset = inset_axes(
    ax, width="20%", height="20%", loc='lower center',
    bbox_to_anchor=(-0.07, 0.1, 1, 1),
    bbox_transform=ax.transAxes
)

# Apply same background to inset
ax_inset.set_facecolor(bg)
ax_inset.set_axisbelow(True)
ax_inset.grid(True, color=grid_color, linewidth=0.8, alpha=0.7)

focus_planets = ["Mars", "Harmonia", "Jupiter"]
focus_indices = [3, 4, 5]
focus_positions = [0, 1, 2]

ax_inset.plot(
    focus_positions,
    [deviation[i] for i in focus_indices],
    'o-', color=indigo, lw=2, markersize=6
)

# Now compute % differences *relative to the empirical optimum a_H^{opt}*
srhf_vs_opt = (lp_srhf / lp_empirical - 1) * 100
pi_vs_opt   = (lp_pi   / lp_empirical - 1) * 100

ax_inset.scatter(1, srhf_vs_opt,
                 color=srhf_algebraic_color, s=80, edgecolor='black', zorder=5)
ax_inset.scatter(1, 0.0,
                 color=crimson, s=80, edgecolor='black', zorder=5)  # empirical optimum is zero reference
ax_inset.scatter(1, pi_vs_opt,
                 color=teal, s=80, edgecolor='black', zorder=5)

# Inset styling
ax_inset.axhline(0, color=gray, linestyle='--', lw=0.8, alpha=0.7)
ax_inset.set_ylim(-0.15, 0.15)  # matches ~±0.07% range but with margin
ax_inset.set_title("Deviation from empirical optimum", fontsize=9, pad=3)
ax_inset.tick_params(axis='both', which='major', labelsize=7)
ax_inset.set_xticks(focus_positions)
ax_inset.set_xticklabels(focus_planets, rotation=35, fontsize=7)

# Inset text annotations (in %)
ax_inset.text(1.1, srhf_vs_opt, f'{srhf_vs_opt:.3f}%', fontsize=6, va='center')
ax_inset.text(1.1, 0.0,        '0.000%',           fontsize=6, va='center')
ax_inset.text(1.1, pi_vs_opt,  f'{pi_vs_opt:.3f}%', fontsize=6, va='center')

# Connection arrow from Harmonia point to inset
con = ConnectionPatch(
    xyA=(lp_index, -0.25),        # in main axes (data coordinates)
    xyB=(0.45, 1.2),              # in inset (axes fraction)
    coordsA="data", coordsB="axes fraction",
    axesA=ax, axesB=ax_inset,
    color="#FF6B6B", linewidth=1.5, alpha=0.6,
    arrowstyle="->,head_width=0.5,head_length=1"
)
ax.add_artist(con)

ax.text(lp_index - 0.4, -0.48, "zoom",
        ha='center', va='bottom',
        fontsize=8, color='gray', alpha=0.7)

plt.savefig("srhf_percent_deviation.png", dpi=300, bbox_inches='tight', facecolor=bg)
plt.show()




