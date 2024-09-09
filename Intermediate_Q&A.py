import tkinter as tk

class BankAccount:
    def __init__(self, balance=30000):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.balance}")
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")
        return self.balance

    def check_balance(self):
        print(f"Balance: {self.balance}")


# Create an instance of BankAccount
account = BankAccount()

while True:
    # User options
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")
    x = int(input("Choose the option: "))

    match x:
        case 1:
            account.check_balance()
        case 2:
            amount = int(input("Withdraw Amount: "))
            account.withdraw(amount)
        case 3:
            amount = int(input("Deposit Amount: "))
            account.deposit(amount)
        case 4:
            exit()
        case _:
            print("Invalid option.")

