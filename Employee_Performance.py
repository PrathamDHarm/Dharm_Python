# Function to add employee details
def add_employee(emp_id, emp_name, emp_dept):
    emp_details = {
        emp_id: {"Name": emp_name, "Department": emp_dept}
    }
    print("Employee:", emp_details[emp_id]['Name'])

# Function to record performance ratings for each month
def record_performance(ratings):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    perfo = {}
    
    # Store the ratings for each month
    for i in range(12):
        perfo[months[i]] = ratings[i]
    
    total = sum(ratings)
    avg = total / 12

    # Print the total and average rating
    print(f"Total Performance Rating: {total}")
    print(f"Average Performance Rating: {avg:.2f}")  # Format average with 2 decimal places

# Input employee details
name = input("Enter employee name: ")
emp_id = int(input("Enter employee ID: "))
dept = input("Enter employee department: ")

ratings = []

# Collect ratings for each of the 12 months
for i in range(12):
    rating = int(input(f"Enter performance score for month {i + 1}: "))
    ratings.append(rating)

# Add employee details and display performance
add_employee(emp_id, name, dept)
record_performance(ratings)
