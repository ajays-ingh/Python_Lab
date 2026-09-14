s = input("Enter any string: ")  # Take input

print("Uppercase", s.upper())  # Convert to uppercase
print("Lower", s.lower())  # Convert to lowercase
print("Reversed", s[::-1])  # Reverse the string

count = 0  # Set count to 0

for char in s.lower():  # Check each character
    if char in 'aeiou':  # Check for vowel
        count += 1

print("Number of vowels", count)  # Print vowel count
   
