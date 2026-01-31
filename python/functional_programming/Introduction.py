# today
# functional programming
# > functions
# > parameter and arguments


# ---------------------------

# python support 3 main programming paradigms - these are the ways to structure and orgnise the code

# 1. sequential programming  - step by step execution of code but you can't reuse the code
# 2. functional programming - function is a block of code that can be reused
# 3. object-oriented programming -
#
# ---------------------------

# 1 - functinal programming -
# function - is a reusable block of code that operations on data
# create a reusable block of code that can be called in multiple places in the program
# syntax -
# it will never execated because there is no function call
# to call the function - function_name() - 'function name()"

# def function_name(parameters):
#      code'
#      body

# normal function
num = int(input("enter a number - "))
squ = num**2
print(squ)

# reusable function code 
# def square():
#     num = int(input("enter a number - "))
#     squ = num**2
#     print(squ)

# def isperfect(): # reusable function to check perfect number inside a block
#     num = int(input("enter a number - "))
#     sum = 0  # sum of i (which are divisible by num)
#     for i in range(1, num): # iterate the numbers from 1 to num to apply logic in it
#         if num % i == 0: # if the reminder is 0
#             sum = sum + i
#     if sum == num:
#         print(f"{num} is a perfect number")
#     else:
#         print(f"{num} is not a perfect number")

# ex  1

def get_data():
    name=input("enter your name - ")
    print(f'hello, {name}')

# function call
get_data()

# timeframe 24:15