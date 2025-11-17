# Asylbek Murzakulov
# November 11, 2025
# Problem 5 – First convert degrees to radians using the formula,
# then use the math module to do the same and compare.
# Formula: radians = degrees * (pi / 180)

import math

deg = float(input("Enter degrees: "))

# Using the formula (with math.pi as the constant π)
rad_formula = deg * (math.pi / 180.0)

# Using the math module convenience function
rad_math = math.radians(deg)

print(f"Radians (formula): {rad_formula}")
print(f"Radians (math.radians): {rad_math}")
print(f"Difference: {abs(rad_formula - rad_math)}")
