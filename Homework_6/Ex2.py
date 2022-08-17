a = str(input())
b = input()
q = 0

for x in a:
    v = a.find(b, q)
    q = v + 1
    if v == -1:
        break
    print("Індекс символу: ", v)
