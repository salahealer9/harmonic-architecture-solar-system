import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar

# Gold–Indigo palette
colors = ["#E3B505", "#3A0CA3", "#4895EF"]

# Constants
A = np.sqrt(2)
B = A + 1
C = 2*A - 1
D = A - 1

# Observed values (AU)
observeds = [5.204, 9.559, 19.185, 30.156, 39.482]

def predict_outer_fixed_ratios(a_lp):
    # Correct ratios relative to Harmonia
    ratios = [
        (1 + A),                    # Jupiter/Harmonia = 2.414
        C * (1 + A),                # Saturn/Harmonia = 4.422
        2 * C * (1 + A),            # Uranus/Harmonia = 8.844  
        (B / D) * (1 + A),          # Neptune/Harmonia = 14.071
        2 * (A + B) * (1 + A)       # Pluto/Harmonia = 18.486
    ]
    
    return [a_lp * ratio for ratio in ratios]

def rmse_fixed_ratios(a_lp):
    preds = predict_outer_fixed_ratios(a_lp)
    return np.sqrt(np.mean([(p - o)**2 for p, o in zip(preds, observeds)]))

# Coarse sweep for visualization
a_lp_range = np.linspace(2.12, 2.18, 1000)
rmses = [rmse_fixed_ratios(a) for a in a_lp_range]

# Find local minimum using brent method with bounds
result = minimize_scalar(rmse_fixed_ratios, bounds=(2.12, 2.18), method='bounded')
optimal_a_lp = result.x
min_rmse = result.fun

# Comparison constants
pi_value = np.pi**(2/3)
celtic_value = (2*A*C)/(1+A)

# Print results
print(f"Optimal a_H: {optimal_a_lp:.9f} AU")
print(f"π^(2/3):      {pi_value:.9f} AU") 
print(f"Celtic:       {celtic_value:.9f} AU")
print(f"Minimum RMSE: {min_rmse:.9f} AU")

# Calculate predictions at optimum
preds_optimal = predict_outer_fixed_ratios(optimal_a_lp)
preds_celtic = predict_outer_fixed_ratios(celtic_value)
preds_pi = predict_outer_fixed_ratios(pi_value)

print("\nPredictions at optimum:")
for i, planet in enumerate(['Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']):
    print(f"{planet}: {preds_optimal[i]:.3f} AU (obs: {observeds[i]:.3f} AU)")

# Plot
plt.figure(figsize=(10, 6))
plt.plot(a_lp_range, rmses, color=colors[1], linewidth=2, label="RMSE vs a_H")
plt.axvline(optimal_a_lp, color='r', linestyle='--', linewidth=2, 
            label=f"Optimal = {optimal_a_lp:.6f} AU")
plt.axvline(pi_value, color='g', linestyle=':', linewidth=2, 
            label=f"π^(2/3) = {pi_value:.6f} AU")
plt.axvline(celtic_value, color='orange', linestyle='-.', linewidth=2, 
            label=f"Celtic = {celtic_value:.6f} AU")
plt.xlabel("Harmonia's Position a_H (AU)", fontsize=12)
plt.ylabel("Root Mean Square Error (AU)", fontsize=12)
plt.title("Harmonic Model Optimization: Finding Harmonia's Position", fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("harmina_optimization_plot.png", dpi=300, bbox_inches='tight')
plt.show()

# Print differences
print(f"\nDifferences from optimum:")
print(f"π^(2/3) difference: {abs(pi_value - optimal_a_lp):.6f} AU ({abs(pi_value - optimal_a_lp)/optimal_a_lp*100:.3f}%)")
print(f"Celtic difference:  {abs(celtic_value - optimal_a_lp):.6f} AU ({abs(celtic_value - optimal_a_lp)/optimal_a_lp*100:.3f}%)")