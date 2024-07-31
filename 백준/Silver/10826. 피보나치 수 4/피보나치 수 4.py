count = int(input())
first = 0
second = 1
sumof = 0

for i in range(1, count):
    sumof  = first + second
    first = second
    second = sumof

if count == 0:
    print(sumof)
else:
    print(second)
