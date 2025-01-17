input("Press Enter to start the game.")
name = input("Enter your name player: ")
print(f"Welcome {name} to Choose-Path.")

answer = input(f"{name} , You are on  Dirt Road. It has come to an end. Do you want to go the left or you wanna go right. \nChoose a path: Type left to go left and Type right to go right: ").lower()

if answer == "left":
    answer = input(f"{name} , You have come at the river. Do you want swim across or walk around it. \nChoose your way: Type swim to swim across the river and Type walk to walk around the river: ").lower()
    if answer == "swim":
        print(f"You washed away!!! {name} , as River was flooded.")
    elif answer == "walk":
        answer = input("You walked for miles but Atlast You found the bridge but it looks wobby. Do you want cross or go right? Type (cross/right): ").lower()
        if answer == "cross":
            answer = input("You crossed the bridge but loosed all you items. Do you want to continue? Type(yes/no): ")
        elif answer == "right":
            print("You choose right at wrong time. You fall from cliff.")
        else:
            print("Invalid Choose! You loose")
    else:
        print("Invalid Choose! You loose")

elif answer == "right":
    answer = input("You have come across the jungle. It looks like it is full of wild animals. Do you want to cross or wait back: ")
    if answer == "cross":
        answer = input("You came to the bridge. Do you want to continue? Type(yes/no): ")
        if answer == "yes":
            print("Bridge was broken! You loose")
        elif answer == "no":
            answer=input("You Found mountain bike ")

    elif answer == "wait":
        print("You choose right at wrong time. You fall from cliff.")
    else:
        print("Invalid Choose! You loose")