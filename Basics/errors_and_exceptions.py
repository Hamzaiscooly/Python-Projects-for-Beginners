# Try-Except Block

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result is:", result)
except ZeroDivisionError:
    print("Oops! You can't divide by zero.")
except ValueError:
    print("Please enter a valid number.")
