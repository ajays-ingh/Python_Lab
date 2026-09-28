# Function to remove the last element
def remove_last(lst):
    lst.pop()  # Removes the last item


my_list = [10, 20, 30, 40]

print("Before function:", my_list)

remove_last(my_list)  # Call the function

print("After function:", my_list)

# Output:
# Original list: [10, 20, 30, 40]
# List after removing last element: [10, 20, 30]
