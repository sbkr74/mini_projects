import random

def roll():
    min_val = 1
    max_val = 6
    val = random.randint(min_val,max_val)

    return val

while True:
    players = input("Enter the number of players [2 - 4]: ")
    if players.isdigit():
        players_num = int(players)
        if 2<= players_num <=4:
            break
        else:
            print("Players must be between [2 - 4].")
    else:
        print("Invalid! Try Again...")

player_score = 0 
max_score = 50
current_score = 0
while player_score<max_score:
    chance = input("Do you want to roll? ['y']:")
    if chance.lower() == "y":
        value = roll()
        print("You rolled ",value)
        current_score+=value
        player_score = current_score
        print("Your current score: ",current_score)
        if value == 1:
            current_score = 0
            print("You lost your score. Now Current Score:",current_score)
            break
    else:
        player_score = current_score
        print("Total score: ",player_score)
        break
