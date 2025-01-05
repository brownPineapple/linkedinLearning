def print_welcome_message():
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("+                               +")
    print("+         The Coffee Shop       +")
    print("+              Welcome          +")
    print("+                               +")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("")
    print("We serve the following coffees:")
    print(" > Espresso")
    print(" > Americano")
    print(" > Latte")
    print(" > Cappuccino")
    print(" > Macchiato")
    print(" > Mocha")
    print(" > Flat White")
    print("----------------------------")


def get_coffee_type():
    coffee_prices = {
        "Espresso": 2.50,
        "Americano": 3.00,
        "Latte": 2.50,
        "Cappuccino": 3.00,
        "Macchiato": 2.50,
        "Mocha": 3.50,
        "Flat White": 2.50
    }
    while True:
        coffee = input("What type of coffee would you like?").title()
        if coffee in coffee_prices:
            return coffee, coffee_prices[coffee]
        else:
            print(f"Invalid option {coffee}")


def get_cup_size():
    size_prices = {
        'M': 0,
        'L': 1,
        'XL': 1.5
    }
    print(f'{coffee} is available in the following sizes: ')
    print(" > M")
    print(" > L")
    print(" > XL")
    print("----------------------------")
    while True:
        size = input("Cup Size: ").upper()
        if size in size_prices:
            return size_prices[size]
        else:
            print('Invalid Cup Size, please try again')


def get_takeaway_option():
    while True:
        takeaway = input("Takeaway ? [Yes/No]").title()
        if takeaway in ['Yes', 'No']:
            return 1 if takeaway == 'Yes' else 0
        else:
            print("Invalid option")


# Main code
print_welcome_message()

price = 0
coffee, coffee_price = get_coffee_type()
price += coffee_price

size_price = get_cup_size()
price += size_price

takeaway_price = get_takeaway_option()
price += takeaway_price

print("----------------------------")
print(f'Total price: ${price:.2f}')
