# factorial_iterative.py
# Calculate factorial of a number using a loop

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {factorial(num)}")
