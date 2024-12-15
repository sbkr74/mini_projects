def add_expense(expenses,description,amount):
    expenses.append({"description":description,"amount":amount})
    print(f"Added expense:{description}, Amount:{amount}")

def main():
    print("Welcome to Budget Tracker")
    initial_budget = float(input("Enter Your Budget for Expense Tracking: "))
    budget = initial_budget
    expenses = []
    while initial_budget>0:
        print("\nWhat you like do?")
        print("1. Add expenses")
        print("2. Show budget details")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3) : ")
        if choice == "1":
            print("-"*25)
            description = input("Enter name of product: ")
            amount = float(input("Enter cost of the product: "))
            add_expense(expenses,description,amount)

        elif choice == "2":
            total = 0
            sign = "₹"
            print("-"*25)
            for expense in expenses:
                total+= expense['amount']                    
                print(expense['description'],expense['amount'])
            print(f"\nTotal Expenditure:{sign}{total} \t Remaining Balance:{sign}{budget-total}")
        
        elif choice == '3':
            print("Goodbye! Signing Off Budget Tracker...\n")
            return False
    
if __name__ == "__main__":
    main()