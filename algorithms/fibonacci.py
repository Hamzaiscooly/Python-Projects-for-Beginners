# fibonacci.py
# Calculates Fibonacci sequence numbers iteratively and recursively

def fibonacci_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fibonacci_rec(n):
    if n <= 1:
        return n
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)

n = 10
print(f"Fibonacci number at position {n} (iterative): {fibonacci_iter(n)}")
print(f"Fibonacci number at position {n} (recursive): {fibonacci_rec(n)}")
