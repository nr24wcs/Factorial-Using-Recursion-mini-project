def factorial(num):
    if num < 0:
        return"Please No ngeative numbers"
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
num = int(input("Please eneter a number:"))

result = factorial(num)
print(f"The factorial of {num} is {result}")