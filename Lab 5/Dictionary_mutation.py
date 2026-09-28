# Function to add a new key-value pair
def add_entry(d):
    d["age"] = 20  # Add new entry


dict = {"name": "Ajay"}

print("Before:", dict)

add_entry(dict)

print("After add_entry:", dict)  

# Output:
# Before function call: {'name': 'Ajay'}
# After function call: {'name': 'Ajay', 'age': 20}



# Function to assign a new dictionary
def reassign_dict(d):
    d = {"city": "Delhi"}  # Creates a new local dictionary


dict = {"name": "Ajay"}

print("Before:", dict)

reassign_dict(dict)

print("After reassign_dict:",dict)

# Output:
# Before function call: {'name': 'Ajay'}
# After function call: {'name': 'Ajay'}