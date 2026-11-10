from functools import reduce

numbers = [5,6,7,8,9]

# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Reduce the list into one value
result = reduce(add_numbers, numbers)

print(result)