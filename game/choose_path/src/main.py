import random
input("Press Enter to start the game.")
name = input("Enter your name player: ")
print(f"Welcome {name.upper()} to Choose-Path.")
days = random.randint(1,20)
answer = input(f"{name.capitalize()} , You are on  Dirt Road. It has come to an end. Do you want to go the left or you wanna go right. \nChoose a path: Type left to go left and Type right to go right: ").lower()

if answer == "left":
    answer = input(f"{name} , You have come at the river. Do you want swim across or walk around it. \nChoose your way: Type swim to swim across the river and Type walk to walk around the river: ").lower()
    if answer == "swim":
        print(f"You washed away!!! {name} , as River was flooded.")
    elif answer == "walk":
        answer = input("You walked for miles but Atlast You found the bridge but it looks wobby. Do you want cross or go right? Type (cross/right): ").lower()
        if answer == "cross":
            answer = input("If You crossed the bridge you will loose all your items. Do you want to continue? Type(yes/no): ").lower()
            if answer == "yes":
                answer = input("You came across cliff. Do you want to proceed! Type go to move forward and back to go back. Type(go/back): ").lower()
                if answer == "go":
                    print("You Fall off the cliff...")
                elif answer == "back":
                    answer = input("Going back from bridge. You reached lake. Do you want to drink water or bath? Type (drink/bath): ").lower()
                    if answer == 'drink':
                        answer = input("Your Thirst is gone. Continue your Journey? Type (Yes/No): ").lower()
                        if answer == 'yes':
                            print('You reached desserted area. You lost in sand and End of the Story.')
                        elif answer == 'no':
                            answer = input("You came across the beach. What you wanna do? ")
                            print(f"You enjoyed your days having {answer} and survived for {days} days.")
                            print("END OF STORY")
                        else:
                            print("Invalid Choose! You loose")
                    elif answer == 'bath':
                        print('You drowned!!! END OF THE ADVENTURE')
                    else:
                        print("Invalid Choose! You loose")
                else:
                    print("Invalid Choose! You loose")
            elif answer == "no":
                print("You try to cross the bridge with your items and due to weigth it broke and you fell down.")
                print("END OF THE STORY")
            else:
                print("Invalid Choose! You loose")

        elif answer == "right":
            print("You choose right at wrong time. You fall from cliff.")
        else:
            print("Invalid Choose! You loose")
    else:
        print("Invalid Choose! You loose")

elif answer == "right":
    answer = input("You have come across the jungle. It looks like it is full of wild animals. Do you want to cross or wait back: Type (cross/wait): ").lower()
    if answer == "cross":
        answer = input("You came to the bridge. Do you want to continue? Type(yes/no): ").lower()
        if answer == "yes":
            print("Bridge was broken! You loose")
        elif answer == "no":
            answer=input("You moved and reached at the end of the road. Wanna travel through Tunnel or glide through jungle. Type (tunnel/glide): ").lower()
            if answer == "tunnel":
                answer = input("You reached at end of tunnel. Choose Left to travel to castle or right to travel to dungeon. Type (left/right)").lower()
                if answer == "left":
                    print("You are trapped in bobby traps. Your Journey came to end")
                elif answer == "right":
                    print("You passed all challenges of Dungeeon. You won Gold!!!")
                else:
                    print("Invalid Choose! You loose")
            elif answer == "glide":
                print("Your glide was struct with lightning. You looose")
            else:
                print("Invalid Choose! You loose")
        else:
            print("Invalid Choose! You loose")
    elif answer == "wait":
        print("You choose right at wrong time. You fall from cliff.")
    else:
        print("Invalid Choose! You loose")