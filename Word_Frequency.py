# Take input from user
s = input("Enter any string: ")

# Split string into words
w = s.split()

# Create empty dictionary
f = {}

# Check each word
for word in w:

    # Check if word is already present
    if word in f:
        f[word] += 1

    # If word is not present
    else:
        f[word] = 1

# Print words and their counts
for word, count in f.items():
    print(word, ":", count)
