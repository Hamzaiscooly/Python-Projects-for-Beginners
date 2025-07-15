# sets.py
# Sets store unique items and support mathematical set operations

# Creating a set
colors = {"red", "green", "blue"}

# Adding items
colors.add("yellow")
print(colors)  # Order may vary

# Duplicate items are ignored
colors.add("red")
print(colors)  # Still no duplicates

# Removing items
colors.remove("green")
print(colors)

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)         # {1, 2, 3, 4, 5, 6}
print("Intersection:", a & b)  # {3, 4}
print("Difference:", a - b)    # {1, 2}
print("Symmetric difference:", a ^ b)  # {1, 2, 5, 6}
