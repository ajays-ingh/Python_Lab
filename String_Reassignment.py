def change_string(s):
    s = "X" + s[1:]
    print("Inside function:", s)

text = "Hello"
print("Before function call:", text)
change_string(text)
print("After function call:", text)