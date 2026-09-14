import string

s = input("Enter any string: ")  # Take input

r = ""  # Empty string

for c in s:
    if c not in string.punctuation:  # Check punctuation
        r += c

print("String without Punctuation", r)  # Print result
