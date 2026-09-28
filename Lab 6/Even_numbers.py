# Generator function to produce even numbers
def even_numbers(limit):
    # Start from 2 and increase by 2
    for num in range(2, limit + 1, 2):
        yield num  # Give one even number at a time


# Print even numbers up to 10
for num in even_numbers(10):
    print(num)
