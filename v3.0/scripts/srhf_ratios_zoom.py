# =====================================================
# SRHF Harmonic Model – Observed/Predicted Ratios (Mars–Pluto)
# Output: srhf_ratios_zoom.png (Figure 6b)
# =====================================================

import numpy as np
import matplotlib.pyplot as plt

planets = ["Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

# Observed semi-major axes (AU) – consistent with the paper
observed = np.array([1.524, 5.204, 9.559, 19.185, 30.156, 39.482])

# Predicted semi-major axes (AU)
# 1) SRHF algebraic prediction (Silver-ratio-based, from Table 1)
pred_srhf = np.array([1.547, 5.172, 9.456, 18.912, 30.142, 39.598])

# 2) Empirically optimised SRHF prediction (using a_H^opt)
#    These values reflect the tuned Harmonia node a_H^{opt} = 2.1437 AU
pred_opt = np.array([1.547, 5.175, 9.463, 18.925, 30.164, 39.627])

# Ratios observed/predicted
ratio_srhf = observed / pred_srhf
ratio_opt  = observed / pred_opt

# =====================================================
# Colours (SRHF palette)
# =====================================================
indigo = "#2B2F8A"        # SRHF algebraic predictions
crimson = "#B22222"       # Empirical optimum

# --- Plot setup ---
fig, ax = plt.subplots(figsize=(10, 6))

# Background and grid color 
bg = "#f8f8f8"
grid_color = "#e0e0e0"
ax.set_facecolor(bg)
fig.patch.set_facecolor(bg)

# Background and grid styling
ax.set_facecolor(bg)
fig.patch.set_facecolor(bg)
ax.set_axisbelow(True)
ax.grid(True, color=grid_color, linewidth=1.0, alpha=0.85)

# SRHF algebraic prediction
ax.plot(
    planets, ratio_srhf, 'o-',
    color=indigo,
    linewidth=2,
    markersize=6,
    label="SRHF harmonic model (algebraic)"
)

# Empirical optimum 
ax.plot(
    planets, ratio_opt, 's--',
    color=crimson,
    linewidth=2,
    markersize=5,
    label="SRHF harmonic model (empirical optimum)"
)

# Reference line at ratio = 1
ax.axhline(1.0, color="gray", linestyle=":", linewidth=1)

# Formatting
ax.set_ylim(0.985, 1.015)
ax.set_ylabel("Observed / Predicted ratio", fontsize=12)
ax.set_xlabel("Planet", fontsize=12)
ax.set_title(
    "SRHF Harmonic Model: Observed/Predicted Ratios (Mars–Pluto)",
    fontsize=13,
    pad=15
)
ax.legend(fontsize=10, loc="upper left")

# Save figure
plt.tight_layout()
plt.savefig("srhf_ratios_zoom.png", dpi=300, bbox_inches='tight', facecolor=bg)
plt.show()