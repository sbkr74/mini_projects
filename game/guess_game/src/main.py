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

guess(10)