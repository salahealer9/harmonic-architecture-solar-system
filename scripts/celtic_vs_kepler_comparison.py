import math
import numpy as np
import sympy as sp

# Define exact symbolic values
sqrt2 = sp.sqrt(2)
sqrt3 = sp.sqrt(3)
sqrt5 = sp.sqrt(5)

A = sqrt2
B = sqrt2 + 1
C = 2*sqrt2 - 1  
D = sqrt2 - 1

kepler_ico_dode = ((sp.sqrt(15) + sp.sqrt(3)) / 4) / (sp.sqrt(250 + 110*sqrt5) / 20)

# Convert symbolic to float for calculations
observed = [0.722/0.387, 1.000/0.722, 1.524/1.000, 5.204/1.524, 9.559/5.204]
observed = [float(x) for x in observed]  # Ensure all are floats

# Kepler predicted ratios (convert to float)
kepler_pred = [
    float(sqrt3), 
    float(kepler_ico_dode), 
    float(kepler_ico_dode), 
    3.000,  # Tetrahedron
    float(sqrt3)
]

# Celtic predicted ratios (convert to float)
celtic_pred = [
    float(C), 
    float(A), 
    float((B + D) / C), 
    float(A / D), 
    float(C)
]

print("Observed ratios:", [f"{x:.3f}" for x in observed])
print("Kepler predictions:", [f"{x:.3f}" for x in kepler_pred])
print("Celtic predictions:", [f"{x:.3f}" for x in celtic_pred])

# Calculate RMSE
kepler_rmse = np.sqrt(np.mean((np.array(observed) - np.array(kepler_pred))**2))
celtic_rmse = np.sqrt(np.mean((np.array(observed) - np.array(celtic_pred))**2))

print(f"\nKepler RMSE: {kepler_rmse:.3f}")
print(f"Celtic RMSE: {celtic_rmse:.3f}")

# Calculate MAPE from the ratios directly
kepler_mape = np.mean(np.abs((np.array(observed) - np.array(kepler_pred)) / np.array(observed))) * 100
celtic_mape = np.mean(np.abs((np.array(observed) - np.array(celtic_pred)) / np.array(observed))) * 100

print(f"Kepler MAPE: {kepler_mape:.2f}%")
print(f"Celtic MAPE: {celtic_mape:.2f}%")