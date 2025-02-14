import random

def guess(x):
    random_guess = random.randint(1,x)
    guess = 0
    while random_guess != guess:
        guess =  int(input(f"Enter the number between 1 to {x}: "))
        if guess<random_guess:
            print("Try Again!! Too Low ...")
        elif guess>random_guess:
            print("Try Again!! Too High.")
    
    print(f"Yay! Congrats, You have guessed the number {random_guess} correctly.")

def computer_guess(x):
    high = x
    low = 1
    user_guess = ""
    while user_guess != "c":
        com_guess = random.randint(low,high)
        user_guess = input(f"Type! If the number {com_guess} is too low[L]/ too high[H]/ correct[C]: ").lower()
        if user_guess == "h":
            high = com_guess-1
        elif user_guess == "l":
            low = com_guess+1
    print(f"Computer has guessed the number {com_guess}")
    

guess(10)
computer_guess(1000)