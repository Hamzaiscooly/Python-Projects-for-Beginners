# List Comprehensions

squares = [x * x for x in range(10)]
print(squares)

# With condition
evens = [x for x in range(10) if x % 2 == 0]
print(evens)