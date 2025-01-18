# WELCOME TO THE VENDING MACHINE 

def display_menu():  # to display the menu
    print("\nWelcome to the Vending Machine!")
    print("First, choose an item based on the corresponding number.")
    categories = set(item['category'] for item in items.values())  
    for category in categories:
        print(f"\n{category.capitalize()} items:")
        for code, item in items.items():
            if item['category'] == category:
                print(f"{code}. {item['name']} - ${item['price']:.2f} (stock: {item['stock']})")

items = {
    '1': {'name': 'Water', 'price': 1.00, 'category': 'beverage', 'stock': 6},
    '2': {'name': 'Pepsi', 'price': 2.50, 'category': 'beverage', 'stock': 5},
    '3': {'name': 'Cheetos', 'price': 3.00, 'category': 'snacks', 'stock': 4},
    '4': {'name': 'Lays', 'price': 1.25, 'category': 'snacks', 'stock': 3},
    '5': {'name': 'Kinder Bueno', 'price': 1.75, 'category': 'chocolate', 'stock': 13},
    '6': {'name': 'Maltesers', 'price': 0.75, 'category': 'chocolate', 'stock': 10},
    '7': {'name': 'London Dairy', 'price': 2.00, 'category': 'icecream', 'stock': 9},
    '8': {'name': 'Igloo', 'price': 1.80, 'category': 'icecream', 'stock': 5},
    '9': {'name': 'Milk Bikis', 'price': 1.20, 'category': 'snacks', 'stock': 8},
    '10': {'name': 'Arrowroot', 'price': 1.50, 'category': 'snacks', 'stock': 3},
    '11': {'name': 'Sprite', 'price': 2.50, 'category': 'beverage', 'stock': 6},
    '12': {'name': 'Coke Zero', 'price': 2.50, 'category': 'beverage', 'stock': 4}
}

def selection_process():
    while True:
        display_menu()
        choice = input("Enter the code number of the chosen item: ")
        
        if choice in items:
            item = items[choice]
            if item['stock'] > 0:
                item_price = item['price']
                print(f"selected {item['name']}, cost of item ${item_price:.2f}.")
                money_inserted = money()
                if money_inserted >= item_price:
                    change = money_inserted - item_price
                    item['stock'] -= 1  
                    print(f"change: ${change:.2f}. thank you for using the vending machine!")
                else:
                    print("error. insufficent funds.")
            else:
                print(f"sorry!, {item['name']} out of stock.")

def money():
    while True:
        try:
            amount = float(input("insert cash: $"))
            if amount > 0:
                return amount
            else:
                print("enter amount.")
        except ValueError:
            print("error. please try again.")


if __name__ == "__main__": #starting the machine
    selection_process()
