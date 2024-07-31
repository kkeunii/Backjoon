count = int(input())
numbers = []

for i in range(count):
    num = list(map(int, input().split()))
    numbers.append(num)

numbers.sort(key = lambda x : (x[1], x[0]))

for i in numbers:
    print(i[0], i[1], end="")
    print()