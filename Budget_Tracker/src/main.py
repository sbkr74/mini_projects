def main():
    print("Welcome to Budget Tracker")
    initial_budget = float(input("Enter Your Budget for Expense Tracking: "))
    
    while True:
        print("What you like do?")
        print("1. Add expenses")
        print("2. Show budget details")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3) : ")
        if choice == "1":
            product = input("Enter name of product: ")
            price = float(input("Enter cost of the product: "))

            initial_budget -= price

        elif choice == "2":
            print("Product:",product,"\t Cost:",price)
            print("Remaining Balance: ",initial_budget)
        
        elif choice == '3':
            return False
    
if __name__ == "__main__":
    main()