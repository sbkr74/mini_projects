def main():
    print("Welcome to Budget tracker App")
    budget = None
    add_expense = None
    try:
        budget = float(input("Enter your proposed budget: "))
    except:
        print("Please Enter Amount in decimal format.")
    while True:
        print("\nWhat do you like do?")
        print("1. Add Expenses")
        print("2. View budget Details")
        print("3. Exit")
        ch = None

        try:
            ch = int(input("Choose the options (1/2/3): "))
        except Exception as e:
            # print(e)                              # Debugging
            print("Error: Only Accepts Integer Value.")

        if ch == 1:
            # add_expense = "Expenses"              # replace it with function
            add_expense = int(input("Enter Amount: "))
        elif ch == 2:
            if add_expense is None:
                print(f"Show budget and all balance!: {budget}")
                print("expenses are not added")
            else:
                view_budget = f"Show Budget {add_expense} and remaining balances: {budget-add_expense}"   # replace it with function
                print(view_budget)
        elif ch == 3:
            print("Exiting from App...")
            break
        else:
            print("Invalid Input! Choose from options...")

main()