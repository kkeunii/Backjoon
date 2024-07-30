import math

count = int(input())
num = list(map(int, input().split()))
numbers = []

for i in num:
    if i == 1:
        continue
    isit = True
    for p in range(2, int(math.sqrt(i)) + 1):
        if i % p == 0:
            isit = False
            break
    if isit:
        numbers.append(i)

print(len(numbers))
