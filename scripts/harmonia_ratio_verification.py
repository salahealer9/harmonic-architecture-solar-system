import numpy as np
import sympy as sp

# Celtic Cross ratios
sqrt2 = sp.sqrt(2)
A = sqrt2
C = 2*sqrt2 - 1

# Harmonia position from combination formula
H = (2 * A * C) / (1 + A)

# Observed distances
obs_mer = 0.387
obs_ven = 0.722  
obs_ear = 1.000
obs_mar = 1.524
obs_h = 2.142  # Celtic theoretical value
obs_jup = 5.204
obs_sat = 9.559

print("VERIFYING TABLE WITH HARMONIA")
print("=" * 50)

# Calculate each ratio
pairs = [
    ("Ven/Mer", obs_ven/obs_mer, float(C), "C"),
    ("Ear/Ven", obs_ear/obs_ven, float(A), "A"), 
    ("Mar/Ear", obs_mar/obs_ear, float((A+1 + A-1)/C), "(B+D)/C"),
    ("H/Mar", obs_h/obs_mar, float(A), "A"),
    ("Jup/H", obs_jup/obs_h, float(A+1), "B"),
    ("Sat/Jup", obs_sat/obs_jup, float(C), "C")
]

deviations = []
for pair, observed, celtic, formula in pairs:
    deviation = (celtic - observed) / observed * 100
    deviations.append(abs(deviation))
    print(f"{pair}: Obs={observed:.3f}, Celtic={celtic:.3f} ({formula}), Dev={deviation:+.2f}%")

print(f"\nMAPE with Harmonia: {np.mean(deviations):.3f}%")