def main():
    print("Welcome to Budget Tracker")
    initial_budget = float(input("Enter Your Budget for Expense Tracking: "))
    product_dict = {}
    i=1
    while initial_budget>0:
        print("What you like do?")
        print("1. Add expenses")
        print("2. Show budget details")
        print("3. Exit")
        # print(product_dict)
        choice = input("Enter your choice (1/2/3) : ")
        if choice == "1":
            product = input("Enter name of product: ")
            quantity = input("Enter in no. of item: ")
            price = float(input("Enter cost of the product: "))
            product_dict[f"{i}. "+product]=f"{quantity}-₹{price}"
            i+=1
            initial_budget -= price

        elif choice == "2":
            for key,val in product_dict.items():
                print("Product:",key,"Price:",val)
        
        elif choice == '3':
            return False
    
if __name__ == "__main__":
    main()