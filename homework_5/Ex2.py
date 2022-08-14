x = int(input())
y = 0
z = 0
while z < x:
    z += 1
    y = z ** 2
    a = y % 10 ** len(str(z))
    if a == z:
        print(z)