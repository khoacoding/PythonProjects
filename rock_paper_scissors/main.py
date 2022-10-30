import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]


while True:
    user_choice = input("Type rock/paper/scissors or 'q' to quit and show result: ").lower()
    if user_choice == "q":
        break
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Please choose available options!")
        continue
    print(f"You choose {user_choice}")

    index = random.randint(0, 2)
    comp_choice = options[index]
    print(f"Computer choose {comp_choice}")

    if (user_choice == "rock" and comp_choice == "scissors") \
            or (user_choice == "scissors" and comp_choice == "paper")\
            or (user_choice == "paper" and comp_choice == "rock"):
        print("You won!")
        user_wins += 1
    elif user_choice == comp_choice:
        print("Draw! (no one get any point)")
    else:
        print("You lost!")
        computer_wins += 1
    print("-------------------------------")

print("Result: \n"
      f"You win {user_wins} time(s).\n"
      f"Computer wins {computer_wins} time(s).")
