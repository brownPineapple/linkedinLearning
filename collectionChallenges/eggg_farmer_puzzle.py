# The Egg Farmer's Puzzle - www.101computing.net/the-egg-farmer-puzzle/

#Complete your code here...

print("EGG FARMER INTERFACE V1")

eggCount = int(input("How many eggs did you pick up this morning ?\nCount:"))

box1, box2 = divmod(eggCount, 12)
breakfastEggs = box2 - 6 if box2 > 6 else box2

print(f'You will need {box1} cartons of 12')

if box2 > 6:
   print("You will need 1 box of 6")
   
plural = 's' if breakfastEggs > 1 else '' 
   
if breakfastEggs > 0:
   print(f"You will have {breakfastEggs} egg{plural} for breakfast") 
