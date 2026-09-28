# Decorator to double the function's result
def double_result(func):
    def wrapper(*args, **kwargs):
        # Call the original function
        result = func(*args, **kwargs)

        # Return double of the result
        return result * 2

    return wrapper


# Applying the decorator
@double_result
def add(a, b):
    # Return the sum of two numbers
    return a + b


print(add(5, 3))
