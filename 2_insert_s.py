from random import randint

n = int(input("enter n: "))
rl = [randint(1, 100) for i in range(n)]
print(rl)

n -= 1

while n >= 1:
    s = rl[n - 1] + rl[n]
    rl.insert(n, s)
    n -= 1

print(rl)
