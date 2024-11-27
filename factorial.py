# Python code​​​​​​‌‌​​​​‌‌​‌​​​​​​‌​​​​‌‌​​ below

def factorial(num):
    if isinstance(num, int):
        if num >= 1:
            fact=1
            for x in range(1,num+1):
                fact = fact*x
            return fact
        elif num == 0:
            return 1
        else:
            return None
    else:
        return None


number = 1
result = factorial(number)
