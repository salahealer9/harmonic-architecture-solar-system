# =====================================================
# SRHF Harmonic Basin Visualization
# Output: srhf_rmse_hsi_basin.png (Figure 3b)
# =====================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar, root_scalar

# Silver Ratio constants (SRHF)
A = np.sqrt(2)
B = A + 1
C = 2*A - 1
D = A - 1

# Observed semi-major axes (AU)
planets = ["Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
observeds = np.array([5.204, 9.559, 19.185, 30.156, 39.482])

# =====================================================
# SRHF outer‐system predictor (same model as script #1)
# =====================================================
def predict_outer(a_H):
    factor = a_H * (1 + A)
    return np.array([
        factor,                    # Jupiter
        factor * C,                # Saturn
        2 * factor * C,            # Uranus
        factor * (B / D),          # Neptune
        2 * factor * (A + B)       # Pluto
    ])

# =====================================================
# RMSE and HSI metrics
# =====================================================
def rmse(a_H):
    preds = predict_outer(a_H)
    return np.sqrt(np.mean((preds - observeds)**2))

def hsi(a_H):
    preds = predict_outer(a_H)
    pct_residuals = (preds - observeds) / observeds * 100
    return np.std(pct_residuals)


# =====================================================
# RMSE-based empirical optimum
# =====================================================
result = minimize_scalar(rmse, bounds=(2.12, 2.16), method='bounded')
a_H_opt = result.x
rmse_opt = result.fun

# SRHF algebraic & transcendental predictions
a_H_silver = (2*A*C) / (1 + A)
a_H_pi = np.pi**(2/3)

# Sweep range for curves
a_range = np.linspace(2.12, 2.16, 2000)
rmse_vals = np.array([rmse(a) for a in a_range])
hsi_vals  = np.array([hsi(a) for a in a_range])

# =====================================================
# Neptune residual zero crossing
# =====================================================
def neptune_residual(a_H):
    return predict_outer(a_H)[3] - observeds[3]

try:
    sol = root_scalar(neptune_residual, bracket=(2.12, 2.16), method='brentq', xtol=1e-12)
    a_H_neptune_zero = sol.root
except Exception:
    # Fallback: linear interpolation
    neptune_resid = np.array([neptune_residual(a) for a in a_range])
    idx = np.where(np.sign(neptune_resid[:-1]) != np.sign(neptune_resid[1:]))[0]
    if len(idx) > 0:
        i = idx[0]
        x0, x1 = a_range[i], a_range[i+1]
        y0, y1 = neptune_resid[i], neptune_resid[i+1]
        a_H_neptune_zero = x0 - y0 * (x1 - x0) / (y1 - y0)
    else:
        a_H_neptune_zero = None

# =====================================================
# Colours (SRHF palette)
# =====================================================
gold = "#D4AF37"
indigo = "#2B2F8A"
teal = "#1F7A8C"
crimson = "#B22222"
srhf_algebraic_color = "#E07A1A"   # gold/amber for SRHF-algebraic marker
dark_gray = "#3A3A3A"

# =====================================================
# Plotting
# =====================================================

fig, ax1 = plt.subplots(figsize=(9, 6.5))

# Background color
bg = "#f8f8f8"
ax1.set_facecolor(bg)
fig.patch.set_facecolor(bg)

ax1.set_axisbelow(True)
ax1.grid(
    True,
    color="#e0e0e0", 
    linewidth=1.0,
    alpha=0.85
)

# RMSE curve (indigo)
ax1.plot(a_range, rmse_vals, color=indigo, linewidth=2.2, label="RMSE (AU)")
ax1.set_xlabel(r"Harmonia semi-major axis $a_H$ (AU)", fontsize=12)
ax1.set_ylabel("RMSE (AU)", color=indigo, fontsize=12)
ax1.tick_params(axis='y', labelcolor=indigo)
ax1.set_xlim(2.12, 2.16)
ax1.set_facecolor('#f8f8f8')
fig.patch.set_facecolor('#f8f8f8')

# Empirical optimum
ax1.axvline(a_H_opt, color=crimson, linestyle='--', linewidth=1.8)
ax1.text(a_H_opt + 0.0006, max(rmse_vals)*1.00,
         f'$a_H^{{\\mathrm{{opt}}}} = {a_H_opt:.6f}$ AU',
         color=crimson, fontsize=10, va='top')

# HSI on secondary axis (gold)
ax2 = ax1.twinx()
ax2.plot(a_range, hsi_vals, color=gold, linewidth=2.0,
         label="HSI (σ of % residuals)")
ax2.set_ylabel("HSI (σ of % residuals)", color=gold, fontsize=12)
ax2.tick_params(axis='y', labelcolor=gold)

# SRHF algebraic prediction
ax1.axvline(a_H_silver, color=srhf_algebraic_color, linestyle='-.', linewidth=1.6)
ax1.text(a_H_silver - 0.0005, max(rmse_vals)*0.78,
         rf'$a_H^{{\mathrm{{Silver}}}} = {a_H_silver:.6f}$ AU',
         color=srhf_algebraic_color, 
         fontsize=9, ha='right')

# SRHF transcendental prediction
ax1.axvline(a_H_pi, color=teal, linestyle=':', linewidth=1.6)
ax1.text(a_H_pi + 0.0006, max(rmse_vals)*0.78,
         rf'$a_H^{{\pi}} = {a_H_pi:.6f}$ AU',
         color=teal, fontsize=9, va='bottom')

# Neptune sign inversion marker
if a_H_neptune_zero is not None:
    ax1.axvline(a_H_neptune_zero, color=dark_gray, linestyle=":", linewidth=1.2)
    
    ax1.annotate(f"Neptune residual = 0 at {a_H_neptune_zero:.6f} AU",
                 xy=(a_H_neptune_zero, max(rmse_vals) * 0.72),  
                 xytext=(a_H_neptune_zero + 0.003, max(rmse_vals) * 0.72),
                 arrowprops=dict(arrowstyle='->', color=dark_gray, lw=1.2, shrinkA=0, shrinkB=0),
                 color=dark_gray, fontsize=8, ha='left', va='center')

# Combined legend
lines = [
    plt.Line2D([0],[0], color=indigo, lw=2.2),
    plt.Line2D([0],[0], color=gold, lw=2.0),
    plt.Line2D([0],[0], color=crimson, lw=1.8, linestyle='--'),
    plt.Line2D([0],[0], color=srhf_algebraic_color, lw=1.6, linestyle='-.'),
    plt.Line2D([0],[0], color=teal, lw=1.6, linestyle=':')
]
labels = [
    "RMSE (AU)",
    "HSI (σ of % residuals)",
    "Empirical optimum $a_H^{\\mathrm{opt}}$",
    "SRHF algebraic prediction $a_H^{\\mathrm{Silver}}$",
    "SRHF transcendental prediction $a_H^{\\pi}$"
]

ax1.legend(lines, labels, loc='upper center', bbox_to_anchor=(0.34, 0.96),
           ncol=1, frameon=True, fancybox=True, shadow=True, fontsize=9)

ax1.set_title("SRHF Harmonic Basin: RMSE and HSI vs Harmonia Position", fontsize=14)

plt.tight_layout()
plt.savefig("srhf_rmse_hsi_basin.png", dpi=300, bbox_inches='tight')
plt.show()
