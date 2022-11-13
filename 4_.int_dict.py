num = int(input("enter num: "))

l = list(range(1, num + 1))
l_rev = l[::-1]

d = dict(zip(l, l_rev))

print(d)
