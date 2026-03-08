# =====================================================
# Silver-Ratio Harmonic Framework (SRHF)
# Figure 4b: srhf_hsi_values.png
# =====================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

plt.rcdefaults()

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

# --- RMSE as function of a_H ---
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

# --- Predictions at the three a_H values ---
preds_opt    = predict_outer(a_H_opt)
preds_pi     = predict_outer(a_H_pi)
preds_silver = predict_outer(a_H_silver)

# --- Residuals (% deviation) ---
resid_opt    = (preds_opt    - observeds) / observeds * 100
resid_pi     = (preds_pi     - observeds) / observeds * 100
resid_silver = (preds_silver - observeds) / observeds * 100

# --- Harmonic Symmetry Index (HSI = σ of residuals) ---
def harmonic_symmetry_index(residuals_percent):
    return np.std(residuals_percent)

HSI_opt    = harmonic_symmetry_index(resid_opt)
HSI_pi     = harmonic_symmetry_index(resid_pi)
HSI_silver = harmonic_symmetry_index(resid_silver)

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

# Light grey background + white grid behind bars
bg = "#f8f8f8"
plt.rcParams['figure.facecolor'] = bg 
plt.rcParams['axes.facecolor'] = bg 
plt.rcParams['savefig.facecolor'] = bg

x = np.arange(len(planets))
width = 0.25

fig, ax = plt.subplots(figsize=(9, 6.5))

ax.set_facecolor(bg)
fig.patch.set_facecolor(bg)
ax.set_axisbelow(True)
ax.grid(True, color="#e0e0e0", linewidth=1.0, alpha=0.85)

# Bars for each SRHF candidate, with HSI in legend labels
ax.bar(
    x - width, resid_silver, width,
    label=rf"$a_H^{{\mathrm{{Silver}}}}$ (HSI = {HSI_silver:.3f}%)",
    color=srhf_algebraic_color
)
ax.bar(
    x,         resid_opt,    width,
    label=rf"$a_H^{{\mathrm{{opt}}}}$ (HSI = {HSI_opt:.3f}%)",
    color=crimson
)
ax.bar(
    x + width, resid_pi,     width,
    label=rf"$a_H^{{\pi}}$ (HSI = {HSI_pi:.3f}%)",
    color=teal
)

ax.axhline(0, color="grey", linewidth=1, linestyle="--", alpha=0.6)

ax.set_xticks(x)
ax.set_xticklabels(planets, fontsize=11)
ax.set_ylabel("Residual (%)", fontsize=12)
ax.set_title("Planetary Residuals and Harmonic Symmetry Index (HSI)", fontsize=14, pad=14)

ax.legend(frameon=True, fontsize=10, loc="upper left")
# Keep symlog for fine symmetry display, as in your original
ax.set_yscale("symlog")

plt.tight_layout()
plt.savefig("srhf_hsi_values.png", dpi=300, bbox_inches="tight", facecolor=bg)
plt.show()

# =====================================================
# Summary (console)
# =====================================================

print(f"\nOptimal a_H (empirical):           {a_H_opt:.9f} AU")
print(f"a_H^Silver (algebraic SRHF):       {a_H_silver:.9f} AU")
print(f"a_H^pi (π^(2/3), SRHF):            {a_H_pi:.9f} AU")
print(f"Minimum RMSE:                      {min_rmse:.9f} AU")

print("\nHarmonic Symmetry Index (HSI = σ of residuals in %):")
print(f"HSI(a_H^Silver): {HSI_silver:.6f}%")
print(f"HSI(a_H^opt):    {HSI_opt:.6f}%")
print(f"HSI(a_H^pi):     {HSI_pi:.6f}%")
