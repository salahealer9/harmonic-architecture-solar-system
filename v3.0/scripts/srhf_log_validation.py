# =====================================================
# SRHF Harmonic Model – Log-scale Validation
# Observed vs SRHF-Predicted Semi-Major Axes
# Output: srhf_log_validation.png (Figure 7b)
# =====================================================

import numpy as np
import matplotlib.pyplot as plt

# --- Constants for SRHF (Silver Ratio Harmonic Framework) ---
A = np.sqrt(2)
B = A + 1
C = 2*A - 1
D = A - 1

# --- Harmonia positions ---
lp_empirical = 2.1437                # empirical optimum (reference)
lp_pi        = np.pi**(2/3)          # transcendental attractor
lp_srhf      = (2*A*C)/(1 + A)       # SRHF algebraic prediction

# --- Observed semi-major axes (AU) ---
planets = ["Mercury", "Venus", "Earth", "Mars",
           "Harmonia", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

a_obs = np.array([
    0.387, 0.722, 1.000, 1.524,
    lp_empirical,     # Harmonia (reference)
    5.204, 9.559, 19.185, 30.156, 39.482
])

# --- SRHF-predicted semi-major axes (AU) ---
a_srhf = np.array([
    (14/15)*D,        # Mercury
    1/A,              # Venus
    1.0,              # Earth
    (B + D) / C,      # Mars
    (2*A*C)/(1 + A),  # Harmonia
    2*A*C,            # Jupiter
    2*A*C**2,         # Saturn
    4*A*C**2,         # Uranus
    2*A*C*(B/D),      # Neptune
    4*A*C*(A + B)     # Pluto
])

# --- Percent deviation (for text box) ---
deviation = (a_srhf / a_obs - 1) * 100
MAPE = np.mean(np.abs(deviation))

# --- Colors (SRHF palette) ---
indigo = "#2B2F8A"
robin_egg_blue = "#1FCECB"

# --- Background style (consistent with all figures) ---
bg = "#f8f8f8"
grid_color = "#e0e0e0"

# =====================================================
# PLOT: Observed vs SRHF-predicted (log scale)
# =====================================================

fig, ax = plt.subplots(figsize=(12, 6))
ax.set_facecolor(bg)
fig.patch.set_facecolor(bg)
ax.set_axisbelow(True)
ax.grid(True, color=grid_color, linewidth=1.0, alpha=0.85, which='both')

# Observed
ax.plot(
    planets, a_obs, 's-', color=robin_egg_blue, lw=2.5, markersize=7,
    alpha=0.9, label="Observed distances"
)

# Predicted (SRHF)
ax.plot(
    planets, a_srhf, 'o--', color=indigo, lw=2.0, markersize=6,
    alpha=0.85, label="SRHF harmonic model (algebraic prediction)"
)

# Logarithmic y-scale
ax.set_yscale("log")

# Labels
ax.set_ylabel("Semi-major Axis (AU)", fontsize=12)
ax.set_xlabel("Planet", fontsize=12)
ax.set_title(
    "Observed vs SRHF-Predicted Planetary Distances (Log Scale)",
    fontsize=14
)
ax.set_xticks(range(len(planets)))
ax.set_xticklabels(planets, rotation=35)

ax.legend(fontsize=10, loc="upper left", frameon=True)

# --- Text box with global model accuracy ---
ax.text(
    0.5, 0.98,
    f"Global MAPE: {MAPE:.2f}%",
    transform=ax.transAxes,
    fontsize=10,
    va="top",
    ha="center",
    bbox=dict(boxstyle="round", facecolor="white", alpha=0.8)
)

plt.tight_layout()
plt.savefig("srhf_log_validation.png", dpi=300, bbox_inches='tight', facecolor=bg)
plt.show()

# =====================================================
# Print numerical reference table
# =====================================================

print("Planetary Distances Comparison:")
print("Planet       | Observed (AU) | SRHF (AU)    | Difference (AU)")
print("-" * 55)
for i, planet in enumerate(planets):
    diff = a_srhf[i] - a_obs[i]
    print(f"{planet:12} | {a_obs[i]:13.3f} | {a_srhf[i]:12.3f} | {diff:14.3f}")

print(f"\nMAPE: {MAPE:.2f}%")
