a = input()
b = input()
c = a + " " + b
while a.isalpha() is not True or b.isalpha() is not True:
    print("No")
    break
if a.isalpha() is True and b.isalpha() is True:
    print(c[::-1].title())

