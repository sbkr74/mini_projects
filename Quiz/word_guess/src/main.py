import random

words = ['python','scala','swift','java','javascript','ruby','rust']
attempts = 3

chosen_word = random.choice(words)
wordplay = ["_" for _ in chosen_word]

while attempts>0 and "_" in wordplay:
    print("\n"+" ".join(wordplay))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index,letter in enumerate(chosen_word):
            if letter == guess:
                wordplay[index] = guess                 # reveal word
    else:
        print("Idiot!!! Wrong guess. Try again...")
        attempts-=1

if '_' not in wordplay:
    print("You guessed the word!")
    print("".join(wordplay))
    print("You Survived!")

else:
    print ("You ran out of attempts. The word was:",chosen_word)
    print ("You lost!")