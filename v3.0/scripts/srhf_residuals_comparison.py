# =====================================================
# Silver-Ratio Harmonic Framework (SRHF) residuals
# Figure 4a: srhf_residuals_comparison.png
# =====================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# --- Constants (SRHF geometry) ---
A = np.sqrt(2)
B = A + 1
C = 2 * A - 1
D = A - 1

# --- Observed planetary distances (AU) ---
planets   = ["Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
observeds = np.array([5.204, 9.559, 19.185, 30.156, 39.482])

# --- SRHF prediction model for outer planets ---
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

# --- RMSE as a function of a_H ---
def rmse(a_H):
    preds = predict_outer(a_H)
    return np.sqrt(np.mean((preds - observeds) ** 2))

# --- Optimisation (empirical optimum a_H^opt) ---
result   = minimize_scalar(rmse, bounds=(2.12, 2.16), method="bounded")
a_H_opt  = result.x
min_rmse = result.fun

# --- Reference Harmonia candidates ---
a_H_pi     = np.pi ** (2 / 3)            # SRHF transcendental prediction
a_H_silver = (2 * A * C) / (1 + A)       # SRHF algebraic Silver-Ratio prediction

# --- Predictions for each choice of a_H ---
preds_opt    = predict_outer(a_H_opt)
preds_pi     = predict_outer(a_H_pi)
preds_silver = predict_outer(a_H_silver)

# --- Percent residuals ---
resid_opt    = (preds_opt    - observeds) / observeds * 100
resid_pi     = (preds_pi     - observeds) / observeds * 100
resid_silver = (preds_silver - observeds) / observeds * 100

# =====================================================
# Colours (SRHF palette)
# =====================================================
indigo = "#2B2F8A"
teal = "#1F7A8C"
crimson = "#B22222"
srhf_algebraic_color = "#E07A1A"   # gold/amber for SRHF-algebraic marker

# =====================================================
# Plotting
# =====================================================

x     = np.arange(len(planets))
width = 0.25

plt.style.use("default")
fig, ax = plt.subplots(figsize=(9, 6.5))

# Light grey background so grid is visible
bg = "#f8f8f8"
ax.set_facecolor(bg)
fig.patch.set_facecolor(bg)
ax.set_axisbelow(True)
ax.grid(True, axis="y", color="#e0e0e0", linewidth=1.0, alpha=0.85)

# Bars: algebraic Silver, empirical optimum, π^(2/3)
ax.bar(x - width, resid_silver, width,
       label=r"$a_H^{\mathrm{Silver}}$", color=srhf_algebraic_color)
ax.bar(x,         resid_opt,    width,
       label=r"$a_H^{\mathrm{opt}}$",    color=crimson)
ax.bar(x + width, resid_pi,     width,
       label=r"$a_H^{\pi}$",    color=teal)

ax.axhline(0, color="grey", linewidth=1, linestyle="--", alpha=0.6)

ax.set_xticks(x)
ax.set_xticklabels(planets, fontsize=11)
ax.set_ylabel("Residual (%)", fontsize=12)
ax.set_title(
    "Planet-by-Planet Residuals for SRHF Harmonia Candidates",
    fontsize=14, pad=14
)

ax.legend(frameon=True, fontsize=10, loc="upper left")
plt.tight_layout()
plt.savefig("srhf_residuals_comparison.png", dpi=300, bbox_inches="tight")
plt.show()

# =====================================================
# Summary (console)
# =====================================================

print(f"\nOptimal a_H (empirical):           {a_H_opt:.9f} AU")
print(f"a_H^Silver (algebraic SRHF):       {a_H_silver:.9f} AU")
print(f"a_H^pi (π^(2/3), SRHF):            {a_H_pi:.9f} AU")
print(f"Minimum RMSE:                      {min_rmse:.9f} AU")
