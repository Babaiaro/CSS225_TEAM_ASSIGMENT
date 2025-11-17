# Asylbek Murzakulov
# November 11, 2025
# Problem 2 – Use random.randint with inclusive bounds.
# This program asks for low and high (inclusive) and prints several random integers
# using random.randint(low, high).

import random

print("random.randint demo (bounds are INCLUSIVE).")
low = int(input("Enter low (int): "))
high = int(input("Enter high (int, must be >= low): "))

if high < low:
    raise ValueError("High must be >= low.")

print("\nFive samples from random.randint(low, high):")
for _ in range(5):
    print(random.randint(low, high))
