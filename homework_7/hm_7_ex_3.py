a = list(input())
b = list(input())
t = 0

o = a + b
for x in o:
    i = o.count(x)
    if i == 1:
        t += 1
print("кількість унікальних значень в списках a та b:", t)
