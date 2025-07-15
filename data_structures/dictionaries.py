# dictionaries.py
# Dictionaries store key-value pairs

# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "courses": ["Math", "Science"]
}

# Accessing values by key
print(student["name"])  # Alice

# Adding or updating values
student["age"] = 21
student["grade"] = "A"
print(student)

# Removing a key-value pair
student.pop("grade")
print(student)

# Looping through dictionary keys and values
for key, value in student.items():
    print(f"{key}: {value}")

# Check if key exists
if "age" in student:
    print("Age is available")
