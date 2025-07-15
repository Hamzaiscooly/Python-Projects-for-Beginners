# File Read/Write

# Write
with open("example.txt", "w") as file:
    file.write("Hello from Python!\n")

# Read
with open("example.txt", "r") as file:
    print(file.read())