import itertools

n, m = map(int, input().split())
numbers = [i for i in range(1, n+1)]

array = itertools.permutations(numbers, m)

for i in array:

    up = True
    for j in range(len(i)-1):
        if i[j] > i[j+1]:
            up = False
            break
    if up:
        for j in i:
            print(j, end = ' ')
        print()
