import tkinter as tk

class BankAccount:
    def __init__(self, balance=30000):
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds!"
        else:
            self.balance -= amount
            return f"Withdrawn: {amount}, New Balance: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposited: {amount}, New Balance: {self.balance}"

    def check_balance(self):
        return f"Balance: {self.balance}"

# Create an instance of BankAccount
account = BankAccount()

def withdraw_amount():
    try:
        amount = int(entry.get())
        result = account.withdraw(amount)
        result_label.config(text=result)
    except ValueError:
        result_label.config(text="Please enter a valid number.")

def deposit_amount():
    try:
        amount = int(entry.get())
        result = account.deposit(amount)
        result_label.config(text=result)
    except ValueError:
        result_label.config(text="Please enter a valid number.")

def check_balance():
    result = account.check_balance()
    result_label.config(text=result)

def prints():
    print("This Intermediate_Q&A File")
win = tk.Tk()
win.title("Bank Account")
win.geometry("300x300")

# Label for instruction
instruction_label = tk.Label(win, text="Enter amount and select an option:")
instruction_label.pack()

# Entry widget for amount input
entry = tk.Entry(win)
entry.pack()

# Buttons for operations
withdraw_button = tk.Button(win, text='Withdraw', background='red', foreground='black', width=25, height=2, command=withdraw_amount)
withdraw_button.pack(pady=5)

deposit_button = tk.Button(win, text='Deposit', background='green', foreground='black', width=25, height=2, command=deposit_amount)
deposit_button.pack(pady=5)

balance_button = tk.Button(win, text='Check Balance', background='blue', foreground='white', width=25, height=2, command=check_balance)
balance_button.pack(pady=5)

# Label to display the result
result_label = tk.Label(win, text="")
result_label.pack(pady=10)

win.mainloop()
