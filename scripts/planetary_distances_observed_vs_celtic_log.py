import numpy as np
import matplotlib.pyplot as plt

# --- Constants (Celtic Cross ratios) ---
A = np.sqrt(2)
B = A + 1
C = 2*A - 1
D = A - 1

# --- Observed semi-major axes (AU) ---
planets = ["Mercury", "Venus", "Earth", "Mars",
           "Harmonia", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]

           # --- Harmonia positions ---
lp_empirical = 2.1437          # empirical optimum (reference)
lp_pi = np.pi**(2/3)           # transcendental attractor
lp_celtic = (2*A*C)/(1+A)      # Celtic geometric prediction

a_obs = np.array([0.387, 0.722, 1.000, 1.524,
                  lp_empirical, 5.204, 9.559, 19.185, 30.156, 39.482])

# --- Celtic model predictions (AU) ---
a_celtic = np.array([
    (14/15)*D,       # Mercury
    1/A,             # Venus
    1.0,             # Earth
    (B+D)/C,         # Mars
    (2*A*C)/(1+A),   # Harmonia
    2*A*C,           # Jupiter
    2*A*C**2,        # Saturn
    4*A*C**2,        # Uranus
    2*A*C*(B/D),     # Neptune
    4*A*C*(A+B)      # Pluto
])

# --- Calculate % deviations ---
deviation = (a_celtic / a_obs - 1) * 100

# --- Harmonia variants ---
lp_index = planets.index("Harmonia")

# --- Colors (gold–indigo palette) ---
gold = "#D4AF37"
indigo = "#2B2F8A"
teal = "#1F7A8C"
gray = "#4D4D4D"

# --- PLOT 1: Percentage Deviation (Original Plot) ---
plt.figure(figsize=(10, 6))
plt.plot(planets, deviation, 'o-', color=indigo, lw=2.2, markersize=6, label="Celtic Cross model")

# Add shaded ±0.72% MAPE band
plt.fill_between(range(len(planets)), -0.72, 0.72, color='gray', alpha=0.15, label='±0.72% global precision')

# Mark Harmonia variants
plt.scatter(lp_index, (lp_celtic/a_obs[lp_index]-1)*100, color=gold, s=90, edgecolor='black', label="Celtic prediction")
plt.scatter(lp_index, (lp_empirical/a_obs[lp_index]-1)*100, color=indigo, s=90, edgecolor='black', label="Empirical optimum")
plt.scatter(lp_index, (lp_pi/a_obs[lp_index]-1)*100, color=teal, s=90, edgecolor='black', label=r"$\pi^{2/3}$ attractor")

# Reference lines
plt.axhline(0, color=gray, linestyle='--', lw=1)
plt.axhline(2, color=gray, linestyle=':', lw=0.8, alpha=0.5)
plt.axhline(-2, color=gray, linestyle=':', lw=0.8, alpha=0.5)

# Labels and styling
plt.ylabel("Deviation from Observed Distance (%)", fontsize=12)
plt.xlabel("Planet", fontsize=12)
plt.title("Percentage Deviation of Celtic Harmonic Model from Observed Planetary Distances", fontsize=14)
plt.xticks(rotation=35)
plt.ylim(-2.5, 2.5)
plt.legend(fontsize=9, loc="upper right", frameon=True)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("planetary_harmonic_percent_deviation_with_LP_MAEBand.pdf", dpi=300)
plt.show()

# --- PLOT 2: Actual Distance Comparison ---
plt.figure(figsize=(12, 6))

# Plot observed distances with thicker line
plt.plot(planets, a_obs, 's-', color='#D4AF37', lw=2.5, markersize=7, 
         label="Observed distances", alpha=0.9)

# Plot Celtic model distances with slightly thinner line
plt.plot(planets, a_celtic, 'o--', color='#2B2F8A', lw=2.0, markersize=6, 
         label="Celtic model predictions", alpha=0.8)

# Labels and styling
plt.ylabel("Semi-major Axis (AU)", fontsize=12)
plt.xlabel("Planet", fontsize=12)
plt.title("Actual Planetary Distances: Observed vs Celtic Harmonic Model Predictions", fontsize=14)
plt.xticks(rotation=35)
plt.yscale('log')  # Use log scale to better visualize the wide range of distances
plt.legend(fontsize=10, loc="upper center", frameon=True)
plt.grid(True, alpha=0.3, which='both')

# Add text box with model performance
plt.text(0.02, 0.98, f'Global MAPE: {np.mean(np.abs(deviation)):.2f}%', 
         transform=plt.gca().transAxes, fontsize=10,
         verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

plt.tight_layout()
plt.savefig("planetary_distances_observed_vs_celtic_log.pdf", dpi=300)
plt.show()

# Print the actual values for reference
print("Planetary Distances Comparison:")
print("Planet       | Observed (AU) | Celtic (AU)  | Difference (AU)")
print("-" * 55)
for i, planet in enumerate(planets):
    diff = a_celtic[i] - a_obs[i]
    print(f"{planet:12} | {a_obs[i]:13.3f} | {a_celtic[i]:12.3f} | {diff:14.3f}")

    deviation = (a_celtic / a_obs - 1) * 100
mape = np.mean(np.abs(deviation))
print(f"MAPE: {mape:.2f}%")  