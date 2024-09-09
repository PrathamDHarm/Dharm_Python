from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        # Initialize an empty list to store expenses
        self.expenses = []

    # Method to add a new expense
    def add_expense(self, description, amount, date):
        try:
            # Convert date to datetime object to ensure proper format
            expense_date = datetime.strptime(date, '%Y-%m-%d')
            expense = {"Description": description, "Amount": amount, "Date": expense_date}
            self.expenses.append(expense)
            print(f"Expense '{description}' of amount {amount} added on {date}.")
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    # Method to view all expenses, optionally filter by year or month
    def view_expenses(self, year=None, month=None):
        if not self.expenses:
            print("No expenses recorded.")
            return
        
        filtered_expenses = []
        for expense in self.expenses:
            if (year is None or expense["Date"].year == year) and (month is None or expense["Date"].month == month):
                filtered_expenses.append(expense)
        
        if not filtered_expenses:
            print("No expenses found for the specified criteria.")
        else:
            print("Expenses:")
            for expense in filtered_expenses:
                print(f"{expense['Description']} - Amount: {expense['Amount']}, Date: {expense['Date'].strftime('%Y-%m-%d')}")

    # Method to calculate total expenses for a specified period
    def total_expenses(self, year=None, month=None):
        total = 0
        for expense in self.expenses:
            if (year is None or expense["Date"].year == year) and (month is None or expense["Date"].month == month):
                total += expense["Amount"]
        
        print(f"Total expenses for {'year ' + str(year) if year else 'all time'} {'month ' + str(month) if month else ''}: {total}")

    # Method to remove an expense by description
    def remove_expense(self, description):
        for expense in self.expenses:
            if expense["Description"] == description:
                self.expenses.remove(expense)
                print(f"Expense '{description}' removed.")
                return
        print(f"Expense '{description}' not found.")

# Create an instance of the ExpenseTracker class
tracker = ExpenseTracker()

# Add some expenses
tracker.add_expense("Groceries", 50, "2024-08-15")
tracker.add_expense("Electricity Bill", 100, "2024-08-20")
tracker.add_expense("Dinner Out", 30, "2024-07-25")

# View all expenses
tracker.view_expenses()

# View expenses for August 2024
tracker.view_expenses(year=2024, month=8)

# Calculate total expenses for August 2024
tracker.total_expenses(year=2024, month=8)

# Remove an expense
tracker.remove_expense("Dinner Out")

# View all expenses again to confirm removal
tracker.view_expenses()
