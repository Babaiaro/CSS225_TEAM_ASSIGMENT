# Asylbek Murzakulov
# November 11, 2025
# Problem 1 – Use random.randrange with start/stop/step and show example outputs.
# This program asks for start, stop (exclusive), and step, then prints several samples
# using random.randrange to demonstrate the range and stepping behavior.

import random

print("random.randrange demo (stop is EXCLUSIVE).")
start = int(input("Enter start (int): "))
stop = int(input("Enter stop (EXCLUSIVE, int): "))
step = int(input("Enter step (non-zero int, e.g., 1, 2, 5): "))

if step == 0:
    raise ValueError("Step cannot be zero.")

print("\nFive samples from random.randrange(start, stop, step):")
for _ in range(5):
    print(random.randrange(start, stop, step))
