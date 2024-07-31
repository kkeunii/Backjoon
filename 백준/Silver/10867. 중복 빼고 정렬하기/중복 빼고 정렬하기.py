num = int(input())

numbers = list(set(map(int, input().split())))

numbers.sort()

for i in numbers:
    print(i, end = " ")
