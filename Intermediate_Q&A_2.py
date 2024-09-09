class Foods:
    def __init__(self):
        # Initializes a dictionary with prices for various food items
        self.prices = {
            'Coffee': 80,
            'Pizza': 40,
            'Pasta': 50,
            'Salad': 70,
            'Burger': 60
        }

    def cal_price(self, item, quantity):
        # Calculates the total price for a given item and quantity
        if item in self.prices:
            total_price = self.prices[item] * quantity
            return total_price

food = Foods()
total_price = 0

while True:
    # Display the menu with item prices
    print('Coffee: 80\nPizza: 40\nPasta: 50\nSalad: 70\nBurger: 60')
    # Get the user's order
    order = input("Enter your Item Name (or 'Exit' to quit): ").capitalize()

    if order == 'Exit' or order == 'Quit':
        # Exit the loop and display the total price
        print(f"Total Price: Rs{total_price}")
        print("Thank you for your order!")
        break

    if order in food.prices:
        # Get the quantity of the ordered item
        q = int(input("Quantity: "))
        # Calculate the price for the ordered quantity
        price = food.cal_price(order, q)
        if price is not None:
            # Add the calculated price to the total price and display the order details
            total_price += price
            print(f"Added {order}: Quantity: {q} || Price: Rs{price}")
        else:
            print("Item not found")
    else:
        print("Invalid Option")
