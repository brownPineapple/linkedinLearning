cakes = {
  100: ["Carrot", 1.99], 
  101: ["Chocolate", 1.99], 
  102: ["Strawberry", 2.19], 
  103: ["Spice", 2.29], 
  104: ["Vanilla", 1.79],
     105: ["Coffee", 1.49]
  }

result = Answer.build_menu(cakes)

def build_menu(cakes):
  cakes[105] = ["Coffee", 1.49]
  items = []
  for flavor, price in cakes.values():
    items.append(f"{flavor} Cake - ${price}")
  return list(reversed(sorted(items)))
