a = int(input())
b = 0
if 2 < a < 10:
    for x in range(1, a + 1):
        y = list(range(1, x + 1))
        j = y + y[b - 2::-1]
        print(*j)
else:
    print("Mistake")
