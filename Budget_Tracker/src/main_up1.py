def add_expenses():
    item_dict = {}
    item = input("Enter your Product:")
    price = None

    try:
        price = float(input("Enter Price of Product:"))
    except Exception as e:
        # print(e)                                                                       # Debugging
        print("Error: Price input should be decimal")

    item_dict={item:price}
    return item_dict

def view_budget(expense:list): 
    total = 0
    for products in expense:
        for product,val in products.items():
            print(product,val)
            total+=val
    return total
    
def main():
    print("Welcome to Budget tracker App")
    budget = None
    expense = []
    
    try:
        budget = float(input("Enter your proposed budget: "))
    except Exception as e:
        # print(e)                                                                       # Debugging
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
                expend = view_budget(expense)
                print(f"\nTotal expenditure: {expend} and remaining Balance: {budget-expend}")
                
        elif ch == 3:
            print("Exiting from App...")
            break
        else:
            print("Invalid Input! Choose from options...")

main()