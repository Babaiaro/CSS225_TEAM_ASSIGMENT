import random

history = []
print("Welcome to the number guessing game!")
our_random_number = random.randint(1, 100)
print(our_random_number)

for tying in range (0, 100):
    try:
        guessed_number = int(input("\nEnter your guess: "))
    except ValueError:
        print("Please enter a valid number.")
    if guessed_number == our_random_number:
        history.append(guessed_number)
        print(f"Correct! You have guessed number in {tying} tries.")
        q = input("Would you like to play again? (y/n): ")
        if q == "y":
            print("Starting a new game...")
            our_random_number = random.randint(1, 100)
            continue
        elif q == "n":
            if q == "n":
                show_his = input("would you like to see history? (y/n): ")
                if show_his == "y":
                    for i, history in enumerate(history,1):
                        print(i, history)
                elif show_his == "n":
                    print("Thanks for playing! Goodbye!")

            break
        else:
            print("Thank you for playing!")
    elif guessed_number < our_random_number:
        print("Too low! Try again.")
    elif guessed_number > our_random_number:
        print("Too high! Try again.")





