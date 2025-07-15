# nested_structures.py
# Examples of nested data structures in Python

# List of dictionaries
people = [
    {"name": "John", "age": 25},
    {"name": "Jane", "age": 30}
]

for person in people:
    print(f"{person['name']} is {person['age']} years old")

# Dictionary with list values
courses = {
    "Math": ["Algebra", "Calculus"],
    "Science": ["Biology", "Physics"]
}

for subject, topics in courses.items():
    print(f"{subject} includes:")
    for topic in topics:
        print(f" - {topic}")

# Complex nesting
data = {
    "users": [
        {"id": 1, "tags": ["python", "beginner"]},
        {"id": 2, "tags": ["advanced", "oop"]}
    ]
}

for user in data["users"]:
    print(f"User {user['id']} has tags: {', '.join(user['tags'])}")
