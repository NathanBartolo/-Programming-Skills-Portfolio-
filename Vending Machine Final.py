from datetime import datetime

class VendingMachine:
    def __init__(self):
        #Create a dictionary for a vending machine that will input a menu, price and remaining stock
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
                'B9': {'item': 'Croisant', 'price': 2.75, 'stock': 10},
                'B10': {'item': 'Cookies', 'price': 12.50, 'stock': 10},
            },
        }#prompting the remaining money and purchase history
        self.remaining_money = 0
        self.purchase_history = []
#make a function that will display the main vending machine manu layout
    def display_menu(self):
        print("\n----- Vending Machine Menu -----\n")
        for category, items in self.menu.items():
            print(f"{category}:\n")
            print("{:<5} {:<20} {:<10} {:<5}".format("Code", "Item", "Price", "Stock"))
            for code, details in items.items():
                print("{:<5} {:<20} AED {:<10} {:<5}".format(code, details['item'], details['price'], details['stock']))
            print()
    
#creating a function that will ask the user to insert their money into the vending machine
    def insert_money(self):
        while True:
            try:
                self.remaining_money = float(input("\nWelcome to Nathan's Vending Machine!\nPlease insert money in AED: "))
                if self.remaining_money < 0:
                    print("Please insert a positive amount.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
#i also created a function that will ask the user to put the item code for the product that they want
    def select_item(self):
        while True:
            code = input("\nEnter the code of the item you want to purchase (or 'exit' to exit): ")
            if code.lower() == 'exit':
                return None
            elif any(code in items for items in self.menu.values()):
                return code
            else:
                print("Invalid code. Please enter a valid code.")
#this function will tell the user that their product is now dispensing. i also made an if condition that will tell the user that they have insufficient funds.
    def process_purchase(self, code):
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
                    self.purchase_history.append({'item': item['item'], 'price': item['price']})
                    print(f"Dispensing {item['item']}...")
                    print(f"Change: AED {change:.2f}")
                    self.remaining_money -= item['price']

    def suggest_purchase(self):
        if len(self.purchase_history) >= 2:
            last_purchase = self.purchase_history[-1]['item']
            previous_purchase = self.purchase_history[-2]['item']
            if last_purchase == 'Coffee' and previous_purchase != 'Biscuits':
                print("How about adding some biscuits to go with your coffee?")
# function that will help Checking and warning about items that are out of stock
    def check_stock(self):
        for items in self.menu.values():
            for item in items.values():
                if item['stock'] == 0:
                    print(f"Warning: {item['item']} is out of stock!")
# this function is used to ask the user if he want to add more items
    def buy_more(self):
        while True:
            choice = input("\nDo you want to buy more items? (yes/no): ").lower()
            if choice == 'yes':
                return True
            elif choice == 'no':
                return False
            else:
                print("Invalid choice. Please enter 'yes' or 'no'.")
#this function is used to print receipt. i also imported the current time and date for a real time tracking
    def print_receipt(self):
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M:%S")

        print("\n----- Receipt -----\n")
        print(f"Nathan's Vending Machine - {date_time}")
        print("\nItem\t\tPrice")
        total_price = 0
        for purchase in self.purchase_history:
            print(f"{purchase['item']}\t\tAED {purchase['price']:.2f}")
            total_price += purchase['price']
        print("\nTotal Price:\tAED {:.2f}".format(total_price))
        print("\nThank you for using Nathan's Vending Machine!")
#the last function will ask the user if they want to print the receipt or to "go green"
    def run(self):
        while True:
            self.display_menu()
            self.insert_money()
            selected_item = self.select_item()

            if selected_item is None:
                break

            self.process_purchase(selected_item)
            self.suggest_purchase()
            self.check_stock()

            if not self.buy_more():
                break

        print("\nDo you want to print the receipt?")
        print("1. Yes")
        print("2. No (Go Green)")
        choice = input("Enter your choice (1 or 2): ")

        if choice == '1':
            self.print_receipt()


if __name__ == "__main__":
    vending_machine = VendingMachine()
    vending_machine.run()
