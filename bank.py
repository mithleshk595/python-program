class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"₹{amount} withdrawn successfully.")
            else:
                print("Insufficient balance!")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Current balance: ₹{self.balance}")


# Main Program
def main():
    name = input("Enter account holder name: ")
    account = BankAccount(name)

    while True:
        print("\n------ Bank Menu ------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amt = float(input("Enter amount to deposit: "))
            account.deposit(amt)
        elif choice == "2":
            amt = float(input("Enter amount to withdraw: "))
            account.withdraw(amt)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("Thank you for banking with us!")
            break
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
