import math
import sympy as sp
import numpy as np

# ===============================================================
# SYMBOLIC CONSTANTS
# ===============================================================
sqrt2, sqrt3 = sp.sqrt(2), sp.sqrt(3)

# Celtic Cross ratios (exact)
A = sqrt2
B = sqrt2 + 1
C = 2 * sqrt2 - 1
D = sqrt2 - 1

# Kepler’s geometric ratios (exact)
kepler_octa_cube = sp.sqrt(3)  # √3
kepler_tetra = 3
kepler_ico_dode = ((sp.sqrt(15) + sp.sqrt(3)) / 4) / (sp.sqrt(250 + 110 * sp.sqrt(5)) / 20)

# Observed planetary distances (AU)
obs = {
    "Mercury": 0.387,
    "Venus":   0.722,
    "Earth":   1.000,
    "Mars":    1.524,
    "Jupiter": 5.204,
    "Saturn":  9.559
}

# ===============================================================
# RATIO CALCULATIONS
# ===============================================================
print("EXACT CALCULATIONS VERIFICATION")
print("=" * 70)
print(f"{'Ratio':<12} {'Celtic (exact)':<20} {'Celtic (num)':<12} {'Kepler (exact)':<20} {'Kepler (num)':<10}")
print("-" * 70)

ratios_data = [
    ("Ven/Mer", obs["Venus"]/obs["Mercury"],      C,                   kepler_octa_cube),
    ("Ear/Ven", obs["Earth"]/obs["Venus"],        A,                   kepler_ico_dode),
    ("Mar/Ear", obs["Mars"]/obs["Earth"],         (B + D) / C,         kepler_ico_dode),
    ("Jup/Mar", obs["Jupiter"]/obs["Mars"],       A / D,               kepler_tetra),
    ("Sat/Jup", obs["Saturn"]/obs["Jupiter"],     C,                   kepler_octa_cube)
]

for name, obs_ratio, celtic, kepler in ratios_data:
    print(f"{name:<12} "
          f"{sp.latex(celtic):<20} {float(celtic):<12.3f} "
          f"{sp.latex(kepler):<20} {float(kepler):<10.3f}")

# ===============================================================
# DEVIATION CALCULATIONS
# ===============================================================
print("\n" + "=" * 70)
print("DEVIATION CALCULATIONS")
print("=" * 70)
print(f"{'Pair':<12} {'Observed':<10} {'Kepler':<10} {'Celtic':<10} {'K Dev':<10} {'C Dev':<10}")
print("-" * 70)

for name, obs_ratio, celtic, kepler in ratios_data:
    k_dev = (float(kepler) - obs_ratio) / obs_ratio * 100
    c_dev = (float(celtic) - obs_ratio) / obs_ratio * 100
    print(f"{name:<12} {obs_ratio:<10.3f} {float(kepler):<10.3f} {float(celtic):<10.3f} "
          f"{k_dev:<10.1f}% {c_dev:<10.1f}%")

# ===============================================================
# SYMBOLIC VERIFICATION
# ===============================================================
print("\n" + "=" * 70)
print("EXACT SYMBOLIC VALUES")
print("=" * 50)
print(f"A = √2 = {sp.latex(A)}")
print(f"B = √2 + 1 = {sp.latex(B)}")
print(f"C = 2√2 - 1 = {sp.latex(C)}")
print(f"D = √2 - 1 = {sp.latex(D)}")
print(f"Kepler (Octa/Cube) = √3 = {sp.latex(kepler_octa_cube)}")
print(f"Kepler (Ico/Dode) = {sp.latex(kepler_ico_dode.simplify())}")
print(f"Kepler (Tetra) = 3")

print(f"\nNumerical value of Kepler Ico/Dode: {float(kepler_ico_dode):.6f}")
