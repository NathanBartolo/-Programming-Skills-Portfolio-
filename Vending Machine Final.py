# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:31:35 2024

@author: natha
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 23:52:17 2023

@author: natha
"""

from datetime import datetime

class VendingMachine:
    def __init__(self):
        # Create a dictionary for a vending machine that will input a menu, price, and remaining stock
        self.menu = {
            'Drinks': {
                'A1': {'item': 'Coca-Cola', 'price': 1.50, 'stock': 10},
                'A2': {'item': 'Pepsi', 'price': 1.25, 'stock': 10},
                'A3': {'item': 'Starbucks Coffee', 'price': 2.00, 'stock': 10},
                'A4': {'item': 'Laban Up', 'price': 1.75, 'stock': 10},
                'A5': {'item': 'Fanta', 'price': 1.50, 'stock': 10},
                'A6': {'item': 'Karak Tea', 'price': 10.00, 'stock': 10},
                'A7': {'item': 'Water', 'price': 13.00, 'stock': 10},
                'A8': {'item': 'Earl Grey Tea', 'price': 2.50, 'stock': 10},
                'A9': {'item': 'Orange Juice', 'price': 2.25, 'stock': 10},
                'A10': {'item': 'Dragon Fruit Juice', 'price': 2.25, 'stock': 10},
            },
            'Snacks': {
                'B1': {'item': 'Oman Chips', 'price': 1.00, 'stock': 10},
                'B2': {'item': 'Kit-Kat', 'price': 2.00, 'stock': 10},
                'B3': {'item': 'Shawarma', 'price': 7.75, 'stock': 10},
                'B4': {'item': 'Samosa', 'price': 1.50, 'stock': 10},
                'B5': {'item': 'Snickers', 'price': 2.25, 'stock': 10},
                'B6': {'item': 'M&M\'s', 'price': 1.80, 'stock': 9},
                'B7': {'item': 'Bugles', 'price': 1.25, 'stock': 10},
                'B8': {'item': 'Pringles', 'price': 15.50, 'stock': 10},
                'B9': {'item': 'Croissant', 'price': 2.75, 'stock': 10},
                'B10': {'item': 'Cookies', 'price': 12.50, 'stock': 10},
            },
        }  # Prompting the remaining money and purchase history
        self.remaining = 0
        self.data = []

    # Make a function that will display the main vending machine menu layout
    def display(self):
        print("\n----- Vending Machine Menu -----\n")
        for category, items in self.menu.items():
            print(f"{category}:\n")
            print("{:<5} {:<20} {:<10} {:<5}".format("Code", "Item", "Price", "Stock"))
            for code, details in items.items():
                print("{:<5} {:<20} AED {:<10} {:<5}".format(code, details['item'], details['price'], details['stock']))
            print()

    # Creating a function that will ask the user to insert their money into the vending machine
    def transaction(self):
        while True:
            try:
                self.remaining_money = float(input("\nWelcome to Nathan's Vending Machine!\nPlease insert money in AED: "))
                if self.remaining < 0:
                    print("Please insert a positive amount.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

    # I also created a function that will ask the user to put the item code for the product that they want
    def itemselect(self):
        while True:
            code = input("\nEnter the code of the item you want to purchase (or 'exit' to exit): ")
            if code.lower() == 'exit':
                return None
            elif any(code in items for items in self.menu.values()):
                return code
            else:
                print("Invalid code. Please enter a valid code.")

    # This function will tell the user that their product is now dispensing. I also made an if condition that will tell the user that they have insufficient funds.
    def processing(self, code):
        for category, items in self.menu.items():
            if code in items:
                item = items[code]
                if item['stock'] == 0:
                    print(f"Sorry, {item['item']} is out of stock.")
                elif self.remaining_money < item['price']:
                    print("Insufficient funds. Please insert more money.")
                else:
                    print("Now processing...")
                    change = self.remaining_money - item['price']
                    item['stock'] -= 1
                    self.data.append({'item': item['item'], 'price': item['price']})
                    print(f"Dispensing {item['item']}...")
                    print(f"Change: AED {change:.2f}")
                    self.remaining_money -= item['price']

    def suggestion(self):
        if len(self.data) >= 2:
            last_purchase = self.data[-1]['item']
            previous_purchase = self.data[-2]['item']
            if last_purchase == 'Coffee' and previous_purchase != 'Biscuits':
                print("How about adding some biscuits to go with your coffee?")

    # Function that will help check and warn about items that are out of stock
    def checkstock(self):
        for items in self.menu.values():
            for item in items.values():
                if item['stock'] == 0:
                    print(f"Warning: {item['item']} is out of stock!")

    # This function is used to ask the user if he wants to add more items
    def another(self):
        while True:
            choice = input("\nDo you want to buy more items? (yes/no): ").lower()
            if choice == 'yes':
                return True
            elif choice == 'no':
                return False
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")

    # This function is used to print a receipt. I also imported the current time and date for real-time tracking
    def receipt(self):
        now = datetime.now()
        formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")

        print("\n----- Receipt -----\n")
        print(f"Nathan's Vending Machine - {formatted_datetime}")
        print("\nItem\t\tPrice")
        total_price = 0
        for purchase in self.data:
            print(f"{purchase['item']}\t\tAED {purchase['price']:.2f}")
            total_price += purchase['price']
        print("\nTotal Price:\tAED {:.2f}".format(total_price))

        print("\nThank you for using Nathan's Vending Machine!")

    # the last function will ask the user if they want to print the receipt or to "go green"
    def run(self):
        while True:
            self.display()
            self.transaction()
            selected_item = self.itemselect()

            if selected_item is None:
                break

            self.processing(selected_item)
            self.suggestion()
            self.checkstock()

            if not self.another():
                break

        print("\nDo you want to print the receipt?")
        print("1. Yes")
        print("2. No (Go Green)")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            self.receipt()

if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()
