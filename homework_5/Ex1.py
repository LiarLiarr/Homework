num = input()
s = 1
for q in num:
    s = 0
    for f in num:
        if q == f:
            s += 1
    if s > 1:
        print("yes")
        break
else:
    print("No")