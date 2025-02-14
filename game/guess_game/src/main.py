import random

def guess(x):
    random_guess = random.randint(1,x)
    guess = 0
    attempt =0 
    while random_guess != guess:
        guess =  int(input(f"Enter the number between 1 to {x}: "))
        if guess<random_guess:
            print("Try Again!! Too Low ...")
        elif guess>random_guess:
            print("Try Again!! Too High.")
    
    print(f"Yay! Congrats, You have guessed the number {random_guess} correctly. Taken [{attempt} attempts].")

def computer_guess(x):
    high = x
    low = 1
    user_guess = ""
    attempt = 0
    while user_guess != "c":
        attempt+=1
        if low != high:
            com_guess = random.randint(low,high)
        else:
            com_guess = low # either can be right as low == high
        
        user_guess = input(f"Type! If the number {com_guess} is too low[L]/ too high[H]/ correct[C]: ").lower()
        if user_guess == "h":
            high = com_guess-1
        elif user_guess == "l":
            low = com_guess+1
    print(f"Computer has guessed the number {com_guess} in {attempt} attempt.")
    
if __name__ == "__main__":
    print("Which game you want to play")
    print("1. where computer will choose a number and you have to guess the number.")
    print("2. where user will think of a number and computer will guess the number.")
    user_in = int(input("Press 1.> for computer or Press 2.> for user to choose the number."))
    if user_in == 1:
        x = int(input("Input the largest number for range to choose between numbers.(COM): "))
        guess(x)
    elif user_in == 2:
        x = int(input("Input the largest number for range to choose between numbers.(USER): "))
        computer_guess(x)