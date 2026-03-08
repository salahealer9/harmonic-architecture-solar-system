# =====================================================
# SRHF Harmonia Optimisation Script
# Output: srhf_harmonia_optimisation.png (Figure 3a)
# =====================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# Silver Ratio constants (SRHF)
A = np.sqrt(2)
B = A + 1                # δ_S
C = 2*A - 1
D = A - 1

# Observed outer planets (AU)
observeds = [5.204, 9.559, 19.185, 30.156, 39.482]
planet_names = ["Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]


# =====================================================
# SRHF outer-system prediction function
# =====================================================
def predict_outer_fixed_ratios(a_H):
    ratios = [
        (1 + A),                    # Jupiter/Harmonia
        C * (1 + A),                # Saturn/Harmonia
        2 * C * (1 + A),            # Uranus/Harmonia
        (B / D) * (1 + A),          # Neptune/Harmonia
        2 * (A + B) * (1 + A)       # Pluto/Harmonia
    ]
    return [a_H * ratio for ratio in ratios]


# =====================================================
# RMSE computation
# =====================================================
def rmse_fixed_ratios(a_H):
    preds = predict_outer_fixed_ratios(a_H)
    return np.sqrt(np.mean([(p - o)**2 for p, o in zip(preds, observeds)]))


# =====================================================
# Optimisation sweep
# =====================================================
a_H_range = np.linspace(2.12, 2.18, 1000)
rmses = [rmse_fixed_ratios(a) for a in a_H_range]

result = minimize_scalar(rmse_fixed_ratios, bounds=(2.12, 2.18), method='bounded')
optimal_a_H = result.x
min_rmse = result.fun

# SRHF comparison values
srhf_algebraic = (2*A*C) / (1 + A)
srhf_transcendental = np.pi**(2/3)


# =====================================================
# Print summary
# =====================================================
print("\n=== SRHF Harmonia Optimisation Results ===")
print(f"Optimal a_H (empirical):                 {optimal_a_H:.9f} AU")
print(f"SRHF algebraic prediction a_H^Silver:    {srhf_algebraic:.9f} AU")
print(f"SRHF transcendental prediction a_H^π:    {srhf_transcendental:.9f} AU")
print(f"Minimum RMSE:                            {min_rmse:.9f} AU")

# Predictions with empirical optimum
preds_opt = predict_outer_fixed_ratios(optimal_a_H)

print("\nPredicted outer planets at optimum:")
for name, pred, obs in zip(planet_names, preds_opt, observeds):
    print(f"{name:<8}: {pred:.3f} AU   (obs: {obs:.3f} AU)")


# =====================================================
# Colours (SRHF palette)
# =====================================================
indigo = "#2B2F8A"
teal = "#1F7A8C"
crimson = "#B22222"
srhf_algebraic_color = "#E07A1A"   # gold/amber for SRHF-algebraic marker

# =====================================================
# Plot Harmonia optimisation curve
# =====================================================

fig, ax = plt.subplots(figsize=(9, 6.5))

# Background color
bg = "#f8f8f8"
ax.set_facecolor(bg)
fig.patch.set_facecolor(bg)

# Light grey grid behind all elements
ax.set_axisbelow(True)
ax.grid(
    True,
    color="#e0e0e0",      # Same grid color as your other plot
    linewidth=1.0,
    alpha=0.85
)

ax.plot(a_H_range, rmses, color=indigo, linewidth=2, label=r"RMSE vs $a_H$")

# Empirical optimum
ax.axvline(
    optimal_a_H, color=crimson, linestyle='--', linewidth=2,
    label=rf"$a_H^{{\mathrm{{opt}}}} = {optimal_a_H:.6f}\,$AU"
)

# SRHF transcendental prediction
ax.axvline(
    srhf_transcendental, color=teal, linestyle=':', linewidth=2,
    label=rf"$a_H^{{\pi}} = {srhf_transcendental:.6f}\,$AU"
)

# SRHF algebraic prediction
ax.axvline(
    srhf_algebraic, color=srhf_algebraic_color, linestyle='-.', linewidth=2,
    label=rf"$a_H^{{\mathrm{{Silver}}}} = {srhf_algebraic:.6f}\,$AU"
)

ax.set_xlabel(r"Harmonia semi-major axis $a_H$ (AU)", fontsize=12)
ax.set_ylabel("Root Mean Square Error (AU)", fontsize=12)
ax.set_title("SRHF Harmonic Model – Optimisation of Harmonia's Position", fontsize=14)
ax.legend(fontsize=9)

plt.tight_layout()
plt.savefig("srhf_harmonia_optimisation.png", dpi=300, bbox_inches='tight')
plt.show()


# =====================================================
# Differences from optimum
# =====================================================
print("\nDifferences from empirical optimum:")
print(f"Transcendental |a_H^π - a_H^opt|: {abs(srhf_transcendental - optimal_a_H):.6f} AU "
      f"({abs(srhf_transcendental - optimal_a_H) / optimal_a_H * 100:.3f}%)")

print(f"Algebraic      |a_H^Silver - a_H^opt|: {abs(srhf_algebraic - optimal_a_H):.6f} AU "
      f"({abs(srhf_algebraic - optimal_a_H) / optimal_a_H * 100:.3f}%)")
