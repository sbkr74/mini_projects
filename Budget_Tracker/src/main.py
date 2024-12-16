def add_expense(expenses,description,amount):
    expenses.append({"description":description,"amount":amount})
    print(f"Added expense:{description}, Amount:{amount}")

def expense_calculation(expenses):
    total = 0
    for item in expenses:
        total += item['amount']
    return total

def show_budget_details(expenses,budget):
    print("Total Budget: ",budget)
    print("Expenses:")
    for expense in expenses:
        print(f"{expense['description']}\t{expense['amount']}")
    print(f"\nTotal Expenses: {expense_calculation(expenses)}\tRemaining Balance: {budget-expense_calculation(expenses)}")
    
    
def main():
    print("Welcome to Budget Tracker")
    initial_budget = float(input("Enter Your Budget for Expense Tracking: "))
    budget = initial_budget
    expenses = []
    cal = 0 
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
            cal = expense_calculation(expenses)

        elif choice == "2":
            # print("-"*25)
            # print("Expenditure Details of Budget.")
            # for expense in expenses:                  
            #     print(expense['description'],expense['amount'])
            # print(f"\nTotal Expenditure: {cal} \t Remaining Balance: {budget-cal}")
            show_budget_details(expenses,budget)
        
        elif choice == '3':
            print("Goodbye! Signing Off Budget Tracker...\n")
            return False
    
if __name__ == "__main__":
    main()