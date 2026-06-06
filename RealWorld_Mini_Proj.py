class BankAccount:

    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful")
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Balance:", self.balance)

account = BankAccount()

while True:
    print("\n1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        amount = int(input("Enter Amount: "))
        account.deposit(amount)

    elif choice == 2:
        amount = int(input("Enter Amount: "))
        account.withdraw(amount)

    elif choice == 3:
        account.check_balance()

    elif choice == 4:
        break