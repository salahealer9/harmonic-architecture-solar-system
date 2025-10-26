import numpy as np

# Celtic Cross constants
A = np.sqrt(2)
B = A + 1
C = 2*A - 1
D = A - 1

# Observed distances (AU)
observed = {
    'jupiter': 5.204,
    'saturn': 9.559, 
    'uranus': 19.185,
    'neptune': 30.156,
    'pluto': 39.482
}

def calculate_mape(a_H):
    """Calculate MAPE for outer planets given Harmonia position"""
    factor = (a_H * (1 + A)) / (2 * A * C)
    
    predictions = {
        'jupiter': factor * 2 * A * C,
        'saturn': factor * 2 * A * C**2,
        'uranus': factor * 4 * A * C**2,
        'neptune': factor * 2 * A * C * (B / D),
        'pluto': factor * 4 * A * C * (A + B)
    }
    
    errors = []
    for planet in observed:
        error = abs(predictions[planet] - observed[planet]) / observed[planet]
        errors.append(error)
    
    mape = 100 * np.mean(errors)
    return mape, predictions

# Test both positions
print("Geometric position (2.155 AU):")
mape_2155, pred_2155 = calculate_mape(A*1.524)
print(f"MAPE: {mape_2155:.2f}%")

print("\nOptimized position (2.142 AU):")  
mape_2142, pred_2142 = calculate_mape((2 * A * C) / (1+A))
print(f"MAPE: {mape_2142:.2f}%")

print(f"\nImprovement: {mape_2142 - mape_2155:.2f}%")

# Find optimum
print("\nSearching for optimum...")
a_H_range = np.linspace(2.12, 2.25, 1000)
mape_values = [calculate_mape(a)[0] for a in a_H_range]
optimum_index = np.argmin(mape_values)
optimum_aH = a_H_range[optimum_index]
optimum_mape = mape_values[optimum_index]

print(f"Optimum position: {optimum_aH:.4f} AU")
print(f"Minimum MAPE: {optimum_mape:.2f}%")

# Show predictions at optimum
print(f"\nPredictions at optimum ({optimum_aH:.4f} AU):")
opt_mape, opt_pred = calculate_mape(optimum_aH)
for planet in observed:
    error_pct = 100 * (opt_pred[planet] - observed[planet]) / observed[planet]
    print(f"{planet:8}: {opt_pred[planet]:6.3f} AU ({error_pct:+.2f}%)")