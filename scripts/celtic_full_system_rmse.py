import numpy as np

# Celtic Cross constants
A = np.sqrt(2)
B = A + 1
C = 2*A - 1
D = A - 1

# All planetary distances (AU)
distances = {
    'Mercury': 0.387, 'Venus': 0.722, 'Earth': 1.000, 'Mars': 1.524, 'Harmonia': np.sqrt(2)*1.524,
    'Jupiter': 5.204, 'Saturn': 9.559, 'Uranus': 19.185, 
    'Neptune': 30.156, 'Pluto': 39.482
}

# Direct predictions for ALL planets
predictions = {
    'Mercury': (14/15) * D,
    'Venus': 1/A,
    'Earth': 1.000,
    'Mars': (B + D) / C,
    'Harmonia': (2 * A * C)/B,
    'Jupiter': 2 * A * C,
    'Saturn': 2 * A * C**2,
    'Uranus': 4 * A * C**2,
    'Neptune': 2 * A * C * (B / D),
    'Pluto': 4 * A * C * (A + B)
}

print("FULL SYSTEM RMSE CALCULATION:")
print("=" * 50)

squared_errors = []
for planet, pred in predictions.items():
    if planet == 'Earth':
        continue
    empirical = distances[planet]
    error = pred - empirical
    squared_error = error**2
    squared_errors.append(squared_error)
    print(f"{planet}: Error = {error:+.4f} AU, Squared = {squared_error:.6f}")

rmse = np.sqrt(np.mean(squared_errors))
print(f"\nSum of squared errors: {sum(squared_errors):.6f}")
print(f"Mean squared error: {np.mean(squared_errors):.6f}")
print(f"RMSE: {rmse:.6f} AU")

# Compare with outer system only
outer_planets = ['Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
outer_squared_errors = [squared_errors[list(predictions.keys()).index(p)-1] for p in outer_planets]
outer_rmse = np.sqrt(np.mean(outer_squared_errors))

print(f"\nCOMPARISON:")
print(f"Full system RMSE: {rmse:.3f} AU")
print(f"Outer system only RMSE: {outer_rmse:.3f} AU")