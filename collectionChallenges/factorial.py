num = int(input('Enter a number: '))
factorial = 1

print(f'Factorial\n{num}! = ',end='')

for i in range(num,0, -1):
   factorial = factorial*i
   if i == 1:
      print(f'{i}')
   else:
      print(f'{i} x ', end='')
      
print(f'{num}! = {factorial}')
