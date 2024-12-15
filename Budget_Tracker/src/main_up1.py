def add_expenses():
    item_Dict = {}
    item = input("Enter your Product:")
    price = None
    
    try:
        price = float(input("Enter Price of Product:"))
    except:
        print("Error: Price input should be decimal")

    item_Dict={item:price}
    return item_Dict

def main():
    print("Welcome to Budget tracker App")
    budget = None
    expense = []
    
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
            expense.append(add_expenses())
        elif ch == 2:
            if len(expense)==0:
                print(f"Show budget and all balance!: {budget}")
                print("expenses are not added")
            else:
                print("Items Price")
                print("-"*15)
                cal = 0
                for product in expense:
                    for item,val in product.items():
                        print(item,val)
                        cal += val 
                print(f"\nTotal expenditure: {cal} and remaining Balance: {budget-cal}")
        elif ch == 3:
            print("Exiting from App...")
            break
        else:
            print("Invalid Input! Choose from options...")

main()