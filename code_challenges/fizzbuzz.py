# fizzbuzz.py
# Prints numbers 1 to 100 with special rules:
# - multiples of 3 print "Fizz"
# - multiples of 5 print "Buzz"
# - multiples of both print "FizzBuzz"

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
