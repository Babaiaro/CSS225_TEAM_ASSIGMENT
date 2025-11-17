# Asylbek Murzakulov
# November 11, 2025
# Problem 4 – Approximate PI in code, then print math.pi for comparison.
# We use the Nilakantha series for faster convergence:
#   π ≈ 3 + 4/(2·3·4) - 4/(4·5·6) + 4/(6·7·8) - ...
# Then we print Python's math.pi and the absolute error.

import math

terms = int(input("How many Nilakantha terms to sum? (e.g., 10000): "))

pi_approx = 3.0
sign = 1.0
n = 2
for _ in range(terms):
    pi_approx += sign * (4.0 / (n * (n + 1) * (n + 2)))
    sign *= -1.0
    n += 2

print(f"Approx PI (Nilakantha, {terms} terms): {pi_approx}")
print(f"math.pi:                              {math.pi}")
print(f"Absolute error:                       {abs(pi_approx - math.pi)}")
