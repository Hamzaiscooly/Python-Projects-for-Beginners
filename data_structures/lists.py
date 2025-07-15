# lists.py
# Demonstrates creating and using lists in Python

# Creating a list
fruits = ["apple", "banana", "cherry"]

# Accessing items by index (starts at 0)
print(fruits[0])  # apple

# Adding items
fruits.append("orange")
print(fruits)  # ['apple', 'banana', 'cherry', 'orange']

# Inserting at a specific position
fruits.insert(1, "kiwi")
print(fruits)  # ['apple', 'kiwi', 'banana', 'cherry', 'orange']

# Removing items
fruits.remove("banana")
print(fruits)  # ['apple', 'kiwi', 'cherry', 'orange']

# Looping through a list
for fruit in fruits:
    print(f"I like {fruit}")

# Slicing (getting a sublist)
print(fruits[1:3])  # ['kiwi', 'cherry']

# List length
print(f"Number of fruits: {len(fruits)}")
