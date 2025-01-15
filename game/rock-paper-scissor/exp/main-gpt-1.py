import random

print("\nWelcome To Rock-Paper-Scissor Game\n")
print("Instructions:")
print("For Rock, type 'Rock' or 'R'")
print("For Paper, type 'Paper' or 'P'")
print("For Scissor, type 'Scissor' or 'S'")

user_wins = 0
computer_wins = 0

# Define the winning relationships
winning_map = {
    "rock": "scissor",  # Rock beats Scissor
    "scissor": "paper",  # Scissor beats Paper
    "paper": "rock"      # Paper beats Rock
}

options = list(winning_map.keys())

while True:
    user_input = input("\nType Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input == "q":
        print("\nFinal Scores:")
        print("Computer: ", computer_wins)
        print("User: ", user_wins)
        break

    # Map user input to the valid option
    if user_input in ['rock', 'r']:
        user_choice = "rock"
    elif user_input in ['paper', 'p']:
        user_choice = "paper"
    elif user_input in ['scissor', 's']:
        user_choice = "scissor"
    else:
        print("Invalid input, try again.")
        continue

    # Random computer choice
    computer_choice = random.choice(options)

    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {user_choice}")

    # Determine winner using the winning_map dictionary
    if user_choice == computer_choice:
        print("It's a tie!")
    elif winning_map[user_choice] == computer_choice:
        print("You win this round!")
        user_wins += 1
    else:
        print("Computer wins this round!")
        computer_wins += 1
