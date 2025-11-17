# Asylbek Murzakulov
# November 11, 2025
# Problem 6 – Compute factorial two ways:
# (1) Using a loop (the formula n! = 1·2·…·n)
# (2) Using math.factorial
# Then compare the results.

import math

n = int(input("Enter a non-negative integer: "))
if n < 0:
    raise ValueError("n must be non-negative.")

# (1) Loop-based factorial
fact_loop = 1
for k in range(2, n + 1):
    fact_loop *= k

# (2) math.factorial
fact_math = math.factorial(n)

print(f"{n}! (loop): {fact_loop}")
print(f"{n}! (math.factorial): {fact_math}")
print("Match:", fact_loop == fact_math)
