import random

while True:
    user_input = input("Roll the dice: (y/n): ").lower()
    if user_input == "y":
        num_input = input("How many dice do you want to roll: (1 or 2): ").strip()

        if num_input == "1":
            die1 = random.randint(1, 6)
            print(f"({die1}")

        elif num_input == "2":
            die1 = random.randint(1, 6)
            die2 = random.randint(1, 6)
            print(f"({die1}, {die2})")
            if die1 == die2:
                print("You rolled a double!")
                break

        else:
            print("Invalid number of dice. Please choose 1 or 2.")
    elif user_input == "n":
        print("Thank you!")
        break
    else:
        print("Invalid choice!")
