import random

print("\nWelcome To Rock-Paper-Scissor Game\n")
print("Instrcutions:")
print("for Rock Type 'Rock' or 'R'")
print("for Paper Type 'Paper' or 'P'")
print("for Scissor Type 'Scissor' or 'S'")

user_wins = 0
computer_wins = 0

options = ['rock','paper','scissor']
while True:
    user_input = input("\nType Rock/Paper/Scissor or Q to quit: ")
    if user_input.lower() == "q":
        print("Computer: ",computer_wins)
        print("User: ",user_wins)
        break

    com=random.choice(options)
    user=""
    if user_input.lower() in ['rock','r']:
        user=options[0]
    elif user_input.lower() in ['paper','p']:
        user=options[1]
    elif user_input.lower() in ['scissor','s']:
        user=options[2]
    else:
        print("Try again as suggested in Instruction")
        continue

    print("Computer picked: ",com)
    print("You Chose: ",user)
    
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

if computer_wins>user_wins:
    print(f"You Lost against Computer by score of {computer_wins-user_wins}.")
elif computer_wins==user_wins:
    print(f"Game tie at score of {user_wins}.")
else:
    print(f"You won against Computer by {user_wins-computer_wins} score.")