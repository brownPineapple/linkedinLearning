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
    myList = []
    for x in cakes.values():
        for y in x:
            if type(y) is str:
                item = y + " Cake - $"
                continue
            else:
                item = item + str(y)
                
            myList.append(item)
    myList.sort(reverse = True)
    return(myList)
