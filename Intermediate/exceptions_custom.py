# Custom Exception

class CustomError(Exception):
    pass

def risky_function(x):
    if x < 0:
        raise CustomError("Negative value not allowed")
    return x * 2

try:
    print(risky_function(-1))
except CustomError as e:
    print("Caught error:", e)