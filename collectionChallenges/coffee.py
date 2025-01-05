# Print banner
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


price = 0

# Get the type of coffee
while(True):
   coffee = input("What type of coffee would you like?").title()
   match coffee:
      case "Espresso":
         price = price + 2.50
         break
      case "Americano":
         price = price + 3.0
         break
      case "Latte":
         price = price + 2.50
         break
      case "Cappuccino":
         price = price + 3.0
         break
      case "Macchiato":
         price = price + 2.50
         break
      case "Mocha":
         price = price + 3.50
         break
      case "Flat White":
         price = price + 2.50
         break
      case _:
         print(f"Invalid option {coffee}")

# Get cup size
print(f'{coffee} is available in the following sizes: ')
print(" > M")
print(" > L")
print(" > XL")
print("----------------------------")

while(True):
   cup_size = input("Cup Size: ").upper()
   match cup_size:
      case 'M':
         break
      case 'L':
         price = price + 1
         break
      case 'XL':
         price = price + 1.5
         break
      case _:
         print('Invalid Cup Size, please try again')

print("----------------------------")

# Get if customer wants to Takeaway
while(True):
   takeaway = input("Takeaway ? [Yes/No]").title()
   match takeaway:
      case'Yes':
         price = price + 1
         break
      case 'No':
         break
      case _:
         print("Invalid option")
   
print("----------------------------")

print("Total Cost: £" + str(price))
