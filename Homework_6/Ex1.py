a, b = input("Введіть два cлова через пробіл: ").split(" ")

while a.isalpha() is not True or b.isalpha() is not True:
    a, b = input("Введіть два лова через пробіл: ").split(" ")
if a.isalpha() is True and b.isalpha() is True:
    print(a[::-1].title(), b[::-1].title())
