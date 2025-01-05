# The Egg Farmer's Puzzle - www.101computing.net/the-egg-farmer-puzzle/ 

print("EGG FARMER INTERFACE V1") 
# Get the number of eggs picked up 
egg_count = int(input("How many eggs did you pick up this morning?\nCount:")) 

# Calculate the number of cartons of 12 and the remainder 
cartons_of_12, remainder_eggs = divmod(egg_count, 12) 

# Determine the number of breakfast eggs 
breakfast_eggs = remainder_eggs - 6 if remainder_eggs > 6 else remainder_eggs 

# Output the number of cartons of 12 
print(f'You will need {cartons_of_12} cartons of 12') 

# Output if an additional box of 6 is needed 
if remainder_eggs > 6: print("You will need 1 box of 6") 

# Determine the plural form for 'egg' 
plural = 's' if breakfast_eggs != 1 else '' 

# Output the number of breakfast eggs 
if breakfast_eggs > 0:
   print(f"You will have {breakfast_eggs} egg{plural} for breakfast")
