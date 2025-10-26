import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# --- Constants ---
A = np.sqrt(2)
B = A + 1
C = 2*A - 1
D = A - 1

# --- Observed outer planets (AU) ---
planets = ["Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
observeds = np.array([5.204, 9.559, 19.185, 30.156, 39.482])

# --- Prediction model ---
def predict_outer(a_lp):
    factor = a_lp * (1 + A)
    return np.array([
        factor,                    # Jupiter
        factor * C,                # Saturn
        2 * factor * C,            # Uranus
        factor * (B / D),          # Neptune
        2 * factor * (A + B)       # Pluto
    ])

# --- RMSE function ---
def rmse(a_lp):
    preds = predict_outer(a_lp)
    return np.sqrt(np.mean((preds - observeds)**2))

# --- HSI (Harmonic Symmetry Index = std of percentage residuals) ---
def harmonic_symmetry_index(a_lp):
    preds = predict_outer(a_lp)
    residuals = (preds - observeds) / observeds * 100
    return np.std(residuals)

# --- Optimize RMSE ---
result = minimize_scalar(rmse, bounds=(2.12, 2.16), method='bounded')
optimal_a_lp = result.x
min_rmse = result.fun

# --- Key reference values ---
pi_value = np.pi**(2/3)
celtic_value = (2*A*C)/(1+A)

# --- Calculate RMSE and HSI curves ---
a_lp_range = np.linspace(2.12, 2.16, 1000)
rmses = [rmse(a) for a in a_lp_range]
hsis = [harmonic_symmetry_index(a) for a in a_lp_range]

# --- Find minimum HSI ---
min_hsi_idx = np.argmin(hsis)
min_hsi_a_lp = a_lp_range[min_hsi_idx]
min_hsi_value = hsis[min_hsi_idx]

# --- Plot RMSE and HSI curves ---
fig, ax1 = plt.subplots(figsize=(10,6))

color1 = 'tab:blue'
ax1.set_xlabel("Harmonia Position a_H (AU)")
ax1.set_ylabel("RMSE (AU)", color=color1)
ax1.plot(a_lp_range, rmses, color=color1, label="RMSE", linewidth=2)
ax1.tick_params(axis='y', labelcolor=color1)
ax1.axvline(optimal_a_lp, color='r', linestyle='--', label=f"RMSE min = {optimal_a_lp:.6f} AU")

# Secondary axis for HSI
ax2 = ax1.twinx()
color2 = 'tab:orange'
ax2.set_ylabel("HSI (σ of % residuals)", color=color2)
ax2.plot(a_lp_range, hsis, color=color2, label="HSI", linewidth=2)
ax2.tick_params(axis='y', labelcolor=color2)
ax2.axvline(min_hsi_a_lp, color='orange', linestyle=':', label=f"HSI min = {min_hsi_a_lp:.6f} AU")

# Mark key constants
for val, lbl, c in [(pi_value, "π^(2/3)", 'green'), (celtic_value, "Celtic 2AC/(1+A)", 'purple')]:
    ax1.axvline(val, color=c, linestyle='-.', linewidth=1.8, label=f"{lbl} = {val:.6f} AU")

# Combine legends
fig.legend(loc="upper center", bbox_to_anchor=(0.5, 1.12), ncol=3)
plt.title("Harmonic Ladder Optimization\nRMSE and Harmonic Symmetry Index (HSI) vs Harmonia Position", fontsize=13)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# --- Final summary ---
print(f"\nOptimal a_LP (RMSE minimum): {optimal_a_lp:.9f} AU")
print(f"π^(2/3):                    {pi_value:.9f} AU")
print(f"Celtic 2AC/(1+A):           {celtic_value:.9f} AU")
print(f"Minimum RMSE:               {min_rmse:.9f} AU")
print(f"HSI minimum:                {min_hsi_value:.6f}% at a_LP = {min_hsi_a_lp:.6f} AU")
print(f"Difference RMSE vs HSI minima: {abs(optimal_a_lp - min_hsi_a_lp):.6e} AU")
