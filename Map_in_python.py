# Original list
numbers = [7,8,9,10]

# Function to add 2
def add_two(number):
    return number + 2

# Apply map to every element
result = map(add_two, numbers)

# Convert map object into a list
print(list(result))