# Module 4 Team Project – Menu Program

while True:
    print("\n=== Main Menu ===")
    print("1. Say Hello")
    print("2. Show Date")
    print("3. Tell a Joke")
    print("4. Display Team Name")
    print("5. Show Project Info")
    print("0. Exit")

    choice = input("Enter your choice (0-5): ")

    if choice == "1":
        print("You chose 1 – Hello there!")
    elif choice == "2":
        print("You chose 2 – Today's date feature coming soon.")
    elif choice == "3":
        print("You chose 3 – Why do programmers hate bugs? Because they ruin their code!")
    elif choice == "4":
        print("You chose 4 – Team Python Ninjas 🐍")
    elif choice == "5":
        print("You chose 5 – This is our Module 4 project.")
    elif choice == "0":
        print("Exiting program... Goodbye!")
        break
    else:
        print("Invalid choice, please enter a number from 0–5.")
