def add_expenses():
    item_dict = {}
    item = input("Enter your Product:")
    price = None
    try:
        price = float(input("Enter Price of Product:"))
    except:
        print("Error: Price input should be decimal")
    item_dict = {item:price}
    return item_dict

def main():
    print("Welcome to Budget tracker App")
    budget = None
    expense = None
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
            # print(e)                                                                 # Debugging
            print("Error: Only Accepts Integer Value.")

        if ch == 1:
            # expense = float(input("Enter Amount: "))                               # replace it with function
            expense = add_expenses()
        elif ch == 2:
            if expense is None:
                print(f"Show budget and all balance!: {budget}")
                print("expenses are not added")
            else:
                # view_budget = f"Show Expenses: {expense} and remaining balances: {budget-expense}"   # replace it with function
                # print(view_budget)
                for item,val in expense.items():
                    print(item,val)
        elif ch == 3:
            print("Exiting from App...")
            break
        else:
            print("Invalid Input! Choose from options...")

main()