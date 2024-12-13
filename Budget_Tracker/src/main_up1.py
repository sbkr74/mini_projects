def main():
    print("Welcome to Budget tracker App")
    budget = float(input("Please Enter your proposed budget: "))
    while True:
        print("What do you like do?")
        print("1. Add Expenses")
        print("2. View budget Details")
        print("3. Exit")
        ch = int(input("Choose the options (1/2/3): "))
        if ch == 1:
            add_expense = "Expenses"  # replace it with function
        elif ch == 2:
            view_budget = f"Show Budget {add_expense} and remaining balances"   # replace it with function
            print(view_budget)
        elif ch == 3:
            print("Exiting from App...")
            break
        else:
            print("Invalid Input Choose from options...")

main()