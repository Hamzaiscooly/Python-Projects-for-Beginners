# Lambda, Map, and Filter

nums = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x**2, nums))
print("Squares:", squares)

evens = list(filter(lambda x: x % 2 == 0, nums))
print("Evens:", evens)