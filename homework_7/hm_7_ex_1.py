q = [12, 13, 44, 111, 222, 33]
k = 1

for i in range(k, len(q) - 1):
    q[i] = q[i+1]

q.pop()
print(q)
