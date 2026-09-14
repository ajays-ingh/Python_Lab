s=input("Enter any string: ")
w = s.split()
f = {}
for word in w :
    if word in f:
        f[word]+=1
    else:
        f[word]=1
for word , count in f.items():
    print(word,":",count)            