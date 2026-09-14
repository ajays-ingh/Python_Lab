import string
s=input("Enter any string: ")
r = ""
for c in s:
    if c  not in string.punctuation:
        r += c
print("String without Punctuation",r)
