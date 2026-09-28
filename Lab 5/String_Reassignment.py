# Function to change the first character
def change_string(s):
    s = "X" + s[1:]  # Replace first character
    print("Inside function:", s)


my_string = "Hello"

print("Before function:", my_string)

change_string(my_string)

print("After function:", my_string)

# Output:
# Before function call: Hello
# Inside function: Xello
# After function call: Hello