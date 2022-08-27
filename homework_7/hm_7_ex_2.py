q = [1, 5, 12, 65, 98, 11, 13]
k = 0
c = "q"

q.append(0)

for i in range(len(q) - 1, k, -1):
    q[i] = q[i-1]
q[k] = c
print(q)
