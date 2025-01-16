import random

print("\nWelcome To Rock-Paper-Scissor Game\n")

user_wins = 0
computer_wins = 0

options = ['rock','paper','scissor']
while True:
    user_input = input("\nType Rock/Paper/Scissor or Q to quit: ")
    if user_input.lower() == "q":
        print("Computer: ",computer_wins)
        print("User: ",user_wins)
        break

    if user_input not in options:
        continue

    random_num = random.randint(0,2)
    com = options[random_num]
    print("Computer picked: ",com)

    if user_input == com:
        print("It's a tie")
        
    elif user_input == 'rock' and com == 'scissor':
        print("You won")
        user_wins+=1

    elif user_input == 'paper' and com == 'rock':
        print("You won")
        user_wins+=1

    elif user_input == 'scissor' and com == 'paper':
        print("You won")
        user_wins+=1

    else:
        print("You lost")
        computer_wins+=1

if computer_wins>user_wins:
    print(f"You Lost against Computer by score of {computer_wins-user_wins}.")
elif computer_wins==user_wins:
    print(f"Game tie at score of {user_wins}.")
else:
    print(f"You won against Computer by {user_wins-computer_wins} score.")