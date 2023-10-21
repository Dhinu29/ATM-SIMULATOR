class ATM:
    def __init__(self):
        self.balance = 0
        self.transactions = []

    def check_balance(self):
        return f"Your account balance is ${self.balance}"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ${amount}")
            return f"You have successfully deposited ${amount}. Your new balance is ${self.balance}"
        else:
            return "Invalid deposit amount. Please enter a positive amount."

    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")
            return f"You have successfully withdrawn ${amount}. Your new balance is ${self.balance}"
        elif self.balance < amount:
            return "Insufficient funds. Your balance is not enough for this withdrawal."
        else:
            return "Invalid withdrawal amount. Please enter a positive amount."

    def transaction_history(self):
        return "\n".join(self.transactions)

def main():
    atm = ATM()

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Exit")
        choice = input("Please select an option (1/2/3/4/5): ")

        if choice == "1":
            print(atm.check_balance())
        elif choice == "2":
            amount = float(input("Enter the deposit amount: $"))
            print(atm.deposit(amount))
        elif choice == "3":
            amount = float(input("Enter the withdrawal amount: $"))
            print(atm.withdraw(amount))
        elif choice == "4":
            print(atm.transaction_history())
        elif choice == "5":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4/5).")

if __name__ == "__main__":
    main()
