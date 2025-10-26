import numpy as np

# Celtic Cross constants
A = np.sqrt(2)
B = A + 1
C = 2*A - 1
D = A - 1

print("Celtic Cross Constants:")
print(f"A = √2 = {A:.6f}")
print(f"B = A + 1 = {B:.6f}") 
print(f"C = 2A - 1 = {C:.6f}")
print(f"D = A - 1 = {D:.6f}")
print()

# Observed distances (AU) - using optimized 2.155 for Harmonia
distances = {
    'Mercury': 0.387,
    'Venus': 0.722,
    'Earth': 1.000,
    'Mars': 1.524,
    'Harmonia': 2.155,  # Optimized empirical value with geometric extension a_mars*sqrt(2)
    'Jupiter': 5.204,
    'Saturn': 9.559,
    'Uranus': 19.185,
    'Neptune': 30.156,
    'Pluto': 39.482
}

# Celtic Cross predictions
predictions = {
    'Mercury': (14/15) * D,
    'Venus': 1/A,
    'Mars': (B + D) / C,
    'Harmonia': (2 * A * C) / (1 + A),  # Theoretical Celtic ratio
    'Jupiter': 2 * A * C,
    'Saturn': 2 * A * C**2,
    'Uranus': 4 * A * C**2,
    'Neptune': 2 * A * C * (B / D),
    'Pluto': 4 * A * C * (A + B)
}

print("FULL VERIFICATION:")
print("=" * 80)
print(f"{'Planet':<12} {'Celtic Formula':<20} {'Predicted':<10} {'Empirical':<10} {'Deviation':<12}")
print("-" * 80)

for planet in predictions:
    if planet != 'Earth':
        pred = predictions[planet]
        empirical = distances[planet]
        dev = (pred - empirical) / empirical * 100
        
        # Format the formula nicely
        formulas = {
            'Mercury': '(14/15)D',
            'Venus': '1/A', 
            'Mars': '(B+D)/C',
            'Harmonia': '2AC/(1+A)',
            'Jupiter': '2AC',
            'Saturn': '2AC²',
            'Uranus': '4AC²',
            'Neptune': '2AC·(B/D)',
            'Pluto': '4AC(A+B)'
        }
        
        print(f"{planet:<12} {formulas[planet]:<20} {pred:<10.3f} {empirical:<10.3f} {dev:<12.2f}%")

# Calculate MAPE for outer system (Harmonia to Pluto)
outer_planets = ['Harmonia', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']
outer_deviations = []

print(f"\nOUTER SYSTEM ANALYSIS (Harmonia to Pluto):")
print("-" * 50)
for planet in outer_planets:
    pred = predictions[planet]
    empirical = distances[planet]
    dev = abs((pred - empirical) / empirical * 100)
    outer_deviations.append(dev)
    print(f"{planet}: |{dev:.2f}%|")

outer_mape = np.mean(outer_deviations)
print(f"\nOUTER SYSTEM MAPE: {outer_mape:.2f}%")

# Compare theoretical vs optimized Harmonia
print(f"\nHARMONIA COMPARISON:")
print(f"Theoretical Celtic position: {predictions['Harmonia']:.6f} AU")
print(f"Optimized empirical position: {distances['Harmonia']:.6f} AU")
print(f"Difference: {abs(predictions['Harmonia'] - distances['Harmonia']):.6f} AU")
print(f"Relative difference: {abs(predictions['Harmonia'] - distances['Harmonia'])/distances['Harmonia']*100:.2f}%")

# Calculate RMSE for outer system
outer_planets = ['Harmonia', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

squared_errors = []
print("RMSE CALCULATION:")
print("=" * 50)
for planet in outer_planets:
    pred = predictions[planet]
    empirical = distances[planet]
    error = pred - empirical
    squared_error = error**2
    squared_errors.append(squared_error)
    print(f"{planet}: Error = {error:+.4f} AU, Squared = {squared_error:.6f}")

rmse = np.sqrt(np.mean(squared_errors))
print(f"\nSum of squared errors: {sum(squared_errors):.6f}")
print(f"Mean squared error: {np.mean(squared_errors):.6f}")
print(f"RMSE: {rmse:.6f} AU")