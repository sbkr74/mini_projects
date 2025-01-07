import random

def roll():
    min_val = 1
    max_val = 6
    val = random.randint(min_val,max_val)

    return val

while True:
    players = input("Enter the number of players [2 - 4]: ")
    if players.isdigit():
        players = int(players)
        if 2<= players <=4:
            break
        else:
            print("Players must be between [2 - 4].")
    else:
        print("Invalid! Try Again...")

player_score = [0 for _ in range(players)]
max_score = 50
while max(player_score)<max_score:
    for player_idx in range(players):
        print("\nPlayer Number",player_idx+1,"turn has started")
        print("Your Total score is: ",player_score[player_idx],"\n")
        current_score = 0
        
        while True:
            chance = input("Do you want to roll? ['y']:")
            if chance.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                current_score = 0
                print("You rolled ",value)
                print("You lost your streak. Now Current Score:",current_score)
                break
            else:
                print("You rolled ",value)
                current_score+=value

        
            print("Your current score: ",current_score)

        player_score[player_idx] += current_score
        print("Your Total Score is:",player_score[player_idx])

max_score = max(player_score)
winning_idx = player_score.index(max_score)
print(f"Player number {winning_idx+1} is the winner with a score of: {max_score}")