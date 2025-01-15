import random

print("\nWelcome To Rock-Paper-Scissor Game\n")
print("Instructions:")
print("For Rock, type 'Rock' or 'R'")
print("For Paper, type 'Paper' or 'P'")
print("For Scissor, type 'Scissor' or 'S'")

user_wins = 0
computer_wins = 0

options = ['rock', 'paper', 'scissor']

while True:
    user_input = input("\nType Rock/Paper/Scissor or Q to quit: ")
    if user_input.lower() == "q":
        print("\nFinal Scores:")
        print("Computer: ", computer_wins)
        print("User: ", user_wins)
        quit()

    com = random.choice(options)
    user = ""

    if user_input.lower() in ['rock', 'r']:
        user = options[0]
    elif user_input.lower() in ['paper', 'p']:
        user = options[1]
    elif user_input.lower() in ['scissor', 's']:
        user = options[2]
    else:
        print("Invalid input, try again.")
        continue

    print(f"Computer chose: {com}")
    print(f"You chose: {user}")

    # Determine winner based on circular comparison
    user_index = options.index(user)
    com_index = options.index(com)

    if user_index == com_index:
        print("It's a tie!")
    elif (user_index + 1) % len(options) == com_index:
        print("Computer wins this round!")
        computer_wins += 1
    else:
        print("You win this round!")
        user_wins += 1
