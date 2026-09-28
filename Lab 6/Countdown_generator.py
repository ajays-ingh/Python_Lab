# Generator function for counting down from n to 1
def countdown(n):
    while n >= 1:
        yield n  # Give one number at a time
        n -= 1   # Decrease the number


# Print all numbers using a loop
for num in countdown(5):
    print(num)

