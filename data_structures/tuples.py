# tuples.py
# Tuples are like lists but immutable (cannot be changed after creation)

# Creating a tuple
coordinates = (10, 20)

print(coordinates[0])  # 10

# Trying to change a tuple item results in error
# coordinates[0] = 15  # Uncommenting this will cause an error!

# Tuples can be used for multiple return values
def min_max(numbers):
    return (min(numbers), max(numbers))

result = min_max([5, 3, 8, 1])
print(f"Min: {result[0]}, Max: {result[1]}")

# Tuple unpacking
min_val, max_val = result
print(f"Min: {min_val}, Max: {max_val}")
