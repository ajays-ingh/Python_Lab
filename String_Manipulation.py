s=input("Enter any string: ")

print("Uppercase",s.upper())
print("Lower",s.lower())
print("Reversed",s[::-1])

count = 0 
for char in s.lower():
    if char in 'aeiou':
        count+=1
print("Number of vowels",count)    