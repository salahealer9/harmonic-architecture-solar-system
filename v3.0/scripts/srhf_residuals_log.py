# =====================================================
# Silver-Ratio Harmonic Framework (SRHF)
# RMSE/HSI + log residuals
# Output: srhf_residuals_log.png (Figure 5a) 
# =====================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar, root_scalar

# --- Constants (SRHF geometry) ---
A = np.sqrt(2)
B = A + 1
C = 2 * A - 1
D = A - 1

# --- Observed outer planets (AU) ---
planets   = ["Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
observeds = np.array([5.204, 9.559, 19.185, 30.156, 39.482])

# --- SRHF prediction model ---
def predict_outer(a_H):
    """
    Predict outer-planet semi-major axes (AU)
    as a function of the Harmonia node a_H.
    """
    factor = a_H * (1 + A)
    return np.array([
        factor,                    # Jupiter
        factor * C,                # Saturn
        2 * factor * C,            # Uranus
        factor * (B / D),          # Neptune
        2 * factor * (A + B)       # Pluto
    ])

# --- RMSE and HSI definitions ---
def rmse(a_H):
    preds = predict_outer(a_H)
    return np.sqrt(np.mean((preds - observeds) ** 2))

def hsi(a_H):
    preds = predict_outer(a_H)
    residuals_pct = (preds - observeds) / observeds * 100
    return np.std(residuals_pct)

# --- Find empirical optimum (RMSE minimum) ---
result    = minimize_scalar(rmse, bounds=(2.12, 2.18), method="bounded")
a_H_opt   = result.x
opt_rmse  = result.fun

# --- Analytic SRHF candidates ---
a_H_pi     = np.pi ** (2 / 3)           # SRHF transcendental prediction
a_H_silver = (2 * A * C) / (1 + A)      # SRHF algebraic Silver-Ratio prediction

# --- Sample range for curves ---
a_range   = np.linspace(2.12, 2.18, 2000)
rmse_vals = np.array([rmse(a) for a in a_range])
hsi_vals  = np.array([hsi(a)  for a in a_range])

# --- Neptune residual zero crossing (where residual = 0) ---
def neptune_residual(a_H):
    return predict_outer(a_H)[3] - observeds[3]   # Neptune index = 3

try:
    root_result      = root_scalar(neptune_residual, bracket=(2.12, 2.18),
                                   method="brentq", xtol=1e-12)
    a_H_neptune_zero = root_result.root
except Exception:
    a_H_neptune_zero = None

# --- Planet residuals (% of observed) across the ladder ---
residuals_pct = np.array([
    (predict_outer(a) - observeds) / observeds * 100 for a in a_range
])  # shape (len(a_range), 5)

# --- Colour palette ---
gold       = "#D4AF37"
indigo     = "#2B2F8A"
teal       = "#1F7A8C"
crimson    = "#B22222"
srhf_algebraic_color = "#E07A1A"
dark_gray  = "#404040"

planet_colors = {
    "Jupiter": "#4169E1",
    "Saturn":  "#DAA520",
    "Uranus":  "#40E0D0",
    "Neptune": "#4682B4",
    "Pluto":   "#CD5C5C"
}

# =====================================================
# Plotting
# =====================================================

# Light grey background & grid behind artists
bg_color = "#f8f8f8"
plt.rcParams['figure.facecolor'] = bg_color
plt.rcParams['axes.facecolor'] = bg_color

fig, (ax1, ax3) = plt.subplots(
    2, 1, figsize=(9, 9),
    gridspec_kw={"height_ratios": [2.2, 1]}
)

fig.patch.set_facecolor(bg_color)

for ax in (ax1, ax3):
    ax.set_facecolor(bg_color)
    ax.set_axisbelow(True)               
    ax.grid(True, axis="both",
            color="#e0e0e0", linewidth=1.0, alpha=0.85)

# === PANEL 1: RMSE & HSI vs a_H ===
ax2 = ax1.twinx()

# RMSE curve (indigo)
ax1.plot(a_range, rmse_vals, color=indigo, linewidth=2.2, label="RMSE (AU)")
ax1.set_xlabel(r"Harmonia semi-major axis $a_H$ (AU)", fontsize=12, labelpad=-4)
ax1.set_ylabel("RMSE (AU)", color=indigo, fontsize=12)
ax1.tick_params(axis="y", labelcolor=indigo)
ax1.set_xlim(2.12, 2.18)

# HSI curve (gold)
ax2.plot(a_range, hsi_vals, color=gold, linewidth=2.0,
         label="HSI (σ of % residuals)")
ax2.set_ylabel("HSI (σ of % residuals)", color=gold, fontsize=12)
ax2.tick_params(axis="y", labelcolor=gold)

# Vertical markers: a_H^opt, a_H^Silver, a_H^pi, Neptune zero
ax1.axvline(a_H_opt, color=crimson, linestyle="--", linewidth=1.8)
ax1.text(a_H_opt + 0.0006, max(rmse_vals) * 1.00,
         rf"$a_H^{{\mathrm{{opt}}}} = {a_H_opt:.6f}\,\mathrm{{AU}}$",
         color=crimson, fontsize=10, va="top")

ax1.axvline(a_H_silver, color=srhf_algebraic_color, linestyle="-.", linewidth=1.6)
ax1.text(a_H_silver - 0.0005, max(rmse_vals) * 0.78,
         rf"$a_H^{{\mathrm{{Silver}}}} = {a_H_silver:.6f}\,\mathrm{{AU}}$",
         color=srhf_algebraic_color, fontsize=9, ha="right")

ax1.axvline(a_H_pi, color=teal, linestyle=":", linewidth=1.6)
ax1.text(a_H_pi + 0.0006, max(rmse_vals) * 0.78,
         rf"$a_H^{{\pi}} = {a_H_pi:.6f}\,\mathrm{{AU}}$",
         color=teal, fontsize=9, va="bottom")

if a_H_neptune_zero is not None:
    ax1.axvline(a_H_neptune_zero, color=dark_gray, linestyle=":", linewidth=1.2)
    
    ax1.annotate(f"Neptune residual = 0\nat {a_H_neptune_zero:.6f} AU",
                 xy=(a_H_neptune_zero, max(rmse_vals) * 0.72),  
                 xytext=(a_H_neptune_zero + 0.0020, max(rmse_vals) * 0.72),
                 arrowprops=dict(arrowstyle='->', color=dark_gray, lw=1.2, shrinkA=0, shrinkB=0),
                 color=dark_gray, fontsize=8, ha='left', va='center')

# Combined legend (fixed semantics)
lines = [
    plt.Line2D([0], [0], color=indigo,    lw=2.2),
    plt.Line2D([0], [0], color=gold,      lw=2.0),
    plt.Line2D([0], [0], color=crimson,   lw=1.8, linestyle="--"),
    plt.Line2D([0], [0], color=srhf_algebraic_color,lw=1.6, linestyle="-."),
    plt.Line2D([0], [0], color=teal,      lw=1.6, linestyle=":")
]
labels = [
    "RMSE (AU)",
    "HSI (σ of % residuals)",
    r"$a_H^{\mathrm{opt}}$",
    r"$a_H^{\mathrm{Silver}}$",
    r"$a_H^{\pi}$"
]

ax1.legend(
    lines, labels,
    loc="upper left",
    frameon=True, fancybox=True, shadow=True,
    fontsize=9
)

ax1.set_title(
    "SRHF Harmonic Optimization: RMSE & HSI vs Harmonia Position",
    fontsize=14, pad=12
)

# === PANEL 2: Per-planet residual magnitudes (log scale) ===
for i, planet in enumerate(planets):
    ax3.plot(
        a_range, np.abs(residuals_pct[:, i]),
        color=planet_colors[planet],
        linewidth=1.6, label=planet
    )

ax3.set_yscale("log")
ax3.axvline(a_H_opt,    color=crimson,    linestyle="--", linewidth=1.2)
ax3.axvline(a_H_silver, color=srhf_algebraic_color, linestyle="-.", linewidth=1.2)
ax3.axvline(a_H_pi,     color=teal,       linestyle=":", linewidth=1.2)

ax3.set_xlim(2.12, 2.18)
ax3.set_xlabel(r"Harmonia semi-major axis $a_H$ (AU)", fontsize=12)
ax3.set_ylabel(r"$|\mathrm{Residuals}|$ (%) [log scale]", fontsize=12)

ax3.legend(loc="lower left", ncol=1, fontsize=9)
ax3.set_title(
    "Per-planet Residual Magnitudes across SRHF Ladder (log scale)",
    fontsize=12, pad=5
)

plt.tight_layout()
plt.savefig("srhf_residuals_log.png", dpi=300, bbox_inches="tight")
plt.show()

# =====================================================
# Console summary
# =====================================================
print(f"\nOptimal a_H (empirical):           {a_H_opt:.9f} AU")
print(f"a_H^Silver (algebraic SRHF):       {a_H_silver:.9f} AU")
print(f"a_H^pi (π^(2/3), SRHF):            {a_H_pi:.9f} AU")
print(f"Minimum RMSE:                      {opt_rmse:.9f} AU")

if a_H_neptune_zero is not None:
    print(f"Neptune residual = 0 at a_H = {a_H_neptune_zero:.9f} AU")
