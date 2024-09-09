import re
import random

# Initialize a dictionary representing table reservations
tables = {
    'Table-1': {'Seat': 'available', 'Name': '', 'Time': ''},
    'Table-2': {'Seat': 'available', 'Name': '', 'Time': ''},
    'Table-3': {'Seat': 'available', 'Name': '', 'Time': ''},
    'Table-4': {'Seat': 'available', 'Name': '', 'Time': ''},
    'Table-5': {'Seat': 'available', 'Name': '', 'Time': ''}    
}

while True:
    # Prompt user for reservation details and extract time and name using regex
    print("Welcome! Do you have or want to reserve a table?")
    x = input("Enter in this format (Yes, for 7pm under Smith): ")
    match = re.search(r'(\d+pm|\d+am) under (\w+)', x)

    if match:
        time = match.group(1)
        name = match.group(2)
    else:
        print("Invalid format. Please enter the reservation details correctly.")
        exit()

    # Check if a reservation already exists for the given name
    reservation_found = False
    for table, details in tables.items():
        if details.get('Name') == name:
            print(f"{table} is already registered for {name}.")
            details['Seat'] = 'registered'
            details['Time'] = time
            reservation_found = True
            break

    # If no reservation is found, assign a random available table to the user
    if not reservation_found:
        available_tables = [key for key, value in tables.items() if value['Seat'] == 'available']
        if available_tables:
            table_key = random.choice(available_tables)
            tables[table_key]['Name'] = name
            tables[table_key]['Seat'] = 'registered'
            tables[table_key]['Time'] = time
            print(f"{table_key} has been assigned to {name}.")
        else:
            print("Sorry, no available tables.")

    # Code checks user input for reservation details, attempts to match the name to existing reservations, 
    # and assigns a random available table if no reservation is found, updating the tables dictionary accordingly.
