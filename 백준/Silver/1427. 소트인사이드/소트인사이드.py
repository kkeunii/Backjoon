num = input()
numbers = []
for i in num:
    numbers.append(i)


numbers.sort(reverse = True)
number = ""
for p in numbers:
    number += p

print(number)
