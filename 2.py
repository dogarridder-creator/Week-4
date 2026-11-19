balance = 50000

while True:
    print("\n--- ATM Menu ---")
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    
    choice = input("Select an option (1-4): ")

    if choice == "1":
        print(f"Current Balance: Rs. {balance}")
    elif choice == "2":
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid amount! Deposit must be greater than zero.")
        else:
            balance += amount
            print(f"Rs. {amount} deposited. New balance: Rs. {balance}")
    elif choice == "3":
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Invalid amount! Withdrawal must be greater than zero.")
        elif amount > balance:
            print("Insufficient balance! Transaction rejected.")
        else:
            balance -= amount
            print(f"Rs. {amount} withdrawn. Remaining balance: Rs. {balance}")
    elif choice == "4":
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid option! Please choose 1-4.")