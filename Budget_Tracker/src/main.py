def main():
    print("Welcome to Budget Tracker")
    initial_budget = float(input("Enter Your Budget for Expense Tracking: "))
    product_dict = {}
    i=1
    while initial_budget>0:
        print("\nWhat you like do?")
        print("1. Add expenses")
        print("2. Show budget details")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3) : ")
        if choice == "1":
            print("-"*25)
            product = input("Enter name of product: ")
            quantity = input("Enter in no. of item: ")
            price = float(input("Enter cost of the product: "))
            product_dict[f"{i}. "+product]=f"{quantity}->₹{price}"
            i+=1
            initial_budget -= price

        elif choice == "2":
            total =0
            sign = "₹"
            print("-"*25)
            for key,val in product_dict.items():
                print("Product:",key,"Price:",val)
                pos = val.find(sign)
                total += float(val[pos+1:])
            print(f"\nTotal Expenditure:{sign}{total} \t Remaining Balance:{sign}{initial_budget}")
        
        elif choice == '3':
            print("Goodbye! Signing Off Budget Tracker...\n")
            return False
    
if __name__ == "__main__":
    main()