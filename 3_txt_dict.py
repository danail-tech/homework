text = input("enter text: ")
d = {}

for i in text:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

print(d)
