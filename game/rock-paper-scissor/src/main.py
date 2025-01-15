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
        quit()

    com=random.choice(options)
    user=""
    if user_input.lower()=='rock' or user_input.lower()=='r':
        user=options[0]
    elif user_input.lower()=='paper' or user_input.lower()=='p':
        user=options[1]
    elif user_input.lower()=='scissor' or user_input.lower()=='s':
        user=options[2]
    else:
        print("Try again as suggested in Instruction")
        continue

    print("com: ",com)
    print("user: ",user)
    if options.index(com)==options.index(user) :
        print("Draw!!!")
    elif options.index(com)>options.index(user) :
        computer_wins+=1
        print("Computer wins")
    else:
        user_wins+=1
        print("You won")