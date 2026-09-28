# Function to calculate factorial
def factorial(n):

    # Base case for 0 and 1
    if n == 0 or n == 1:
        return 1

    else:
        # Recursive call
        return n * factorial(n - 1)


# Take input from the user
n = int(input("Enter a number to calculate its factorial: "))

# Call the factorial function
result = factorial(n)

# Display the result
print(f"The factorial of {n} is: {result}")


# Output:
# Enter a number to calculate its factorial: 5
# The factorial of 5 is: 120