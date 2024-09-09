import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('C:\\Users\\d.hanumansetty\\OneDrive - Accenture\\Desktop\\python\\coffee.csv')

# Print the entire DataFrame
print(df)
print(df['Coffee Type'])
print("------------------1---------------------------\n")

# Print the first 5 rows of the DataFrame
print(df.head(5))
print("------------------2---------------------------\n")

# Print information about the DataFrame, such as column names, data types, and non-null counts
print(df.info())
print("------------------3---------------------------\n")

# Print summary statistics for numerical columns
print(df.describe())
print("-------------------4--------------------------\n")

# Print the number of unique values in each column
print(df.nunique())
print("-------------------5--------------------------\n")

# Print a random sample of 10 rows from the DataFrame
print(df.sample(10))
print("-------------------6--------------------------\n")

# Print rows 5 to 8 and specific columns 'Day' and 'Coffee Type'
print(df.loc[5:8, ["Day", "Coffee Type"]])
print("-------------------7--------------------------\n")

# Change the value in row 1, column 'Day' to 'Sunday'
df.loc[1, "Day"] = "Sunday"
print("After Changing the first row, column= Day\n", df)
print("-------------------8--------------------------\n")

# Filter and print rows where 'Day' is 'Monday' and 'Coffee Type' is 'Espresso'
print(df[(df['Day'] == 'Monday') & (df['Coffee Type'] == 'Espresso')])
print("--------------------9-------------------------\n")

# Filter and print rows where 'Day' contains 'Sunday' or 'Tuesday' (case-insensitive)
print(df[df['Day'].fillna('').str.contains("sunday|tuesday", case=False)])

print("---------------------10------------------------\n")

# Update the value in row 8, column 'Coffee Type' to 'Strong Coffee'
df.loc[8, 'Coffee Type'] = "Strong Coffee"

# Filter and print rows where 'Coffee Type' contains 'Espresso' or 'Strong Coffee' (case-insensitive)
print(df[df['Coffee Type'].str.contains('Espresso|sTrong Coffee', case=False, regex=True)])
print("----------------------11-----------------------\n")

# Filter and print rows where 'Coffee Type' is either 'Strong Coffee' or 'Latte'
print(df[df['Coffee Type'].isin(['Strong Coffee', 'Latte'])])
print("---------------------12------------------------\n")

print(df.query('`Coffee Type` == "Strong Coffee" and `Day` == "Sunday"'))

# Add a new column 'Price' and assign a price to 'Espresso'
df['Price(USD)'] = None  # Initialize the column with None

# Set price for Espresso
df.loc[df['Coffee Type'] == 'Espresso', 'Price(USD)'] = 3.00  # Assign a price of 3.00 to Espresso

# Set price for Latte
df.loc[df['Coffee Type'] == 'Latte', 'Price(USD)'] = 4.00  # Assign a price of 4.00 to Latte

# Set price for Strong Coffee
df.loc[df['Coffee Type'] == 'Strong Coffee', 'Price(USD)'] = 9.5
print(df)
print("-------------------13--------------------------\n")

# Calculate Coffee Revenue
df['Coffee Revenue'] = df['Units Sold'] * df['Price(USD)']

# Calculate the total revenue
total_units_sold = df['Units Sold'].sum()
total_revenue = df['Coffee Revenue'].sum()
average_price = total_revenue / total_units_sold if total_units_sold else 0

# Append the total as a new row
total_row = pd.DataFrame({
    'Coffee Type': ['Total'],
    'Units Sold': [total_units_sold],
    'Price(USD)': [average_price],
    'Coffee Revenue': [total_revenue]
})
df = pd.concat([df, total_row], ignore_index=True)
print(df)

# Save the modified DataFrame back to the CSV file
df.to_csv('C:\\Users\\d.hanumansetty\\OneDrive - Accenture\\Desktop\\python\\coffee_backup.csv', index=False)

# Scatter plot for Coffee Type vs Units Sold
plt.scatter(df['Coffee Type'], df['Units Sold'])
plt.title('Coffee Type vs Units Sold (Scatter Plot)')
plt.xlabel('Coffee Type')
plt.ylabel('Units Sold')
plt.xticks(rotation=45)
plt.show()

# Line plot for Coffee Type vs Units Sold
df.plot(x='Coffee Type', y='Units Sold', kind='line', title='Coffee Type vs Units Sold (Line Plot)')
plt.xticks(rotation=45)
plt.show()



import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('C:\\Users\\d.hanumansetty\\OneDrive - Accenture\\Desktop\\python\\Book1.csv')

# Calculate the 'Total Average'
df['Total Average'] = (df['Assignement Score'] + df['Exam Score']) / 2

# Loop through the 'Total Average' to assign grades row by row
for i in range(len(df['Total Average'])):
    x = df['Total Average'][i]
    if 90 <= x <= 100:
        df.loc[i, 'Grade'] = 'A'
    elif 80 <= x <= 89:
        df.loc[i, 'Grade'] = 'B'
    elif 70 <= x <= 79:
        df.loc[i, 'Grade'] = 'C'
    elif 60 <= x <= 69:
        df.loc[i, 'Grade'] = 'D'
    else:
        df.loc[i, 'Grade'] = 'F'

# Save the updated DataFrame back to CSV
df.to_csv('C:\\Users\\d.hanumansetty\\OneDrive - Accenture\\Desktop\\python\\Book1.csv', index=False)

# Print to verify the result
print(df)

# Calculate average marks per grade
grade_avg = df.groupby('Grade')['Total Average'].mean()

# Plotting the bar chart
plt.scatter(grade_avg.index, grade_avg)
plt.title("Average Marks per Grade")
plt.xlabel('Grade')
plt.ylabel('Average Marks')
plt.show()




