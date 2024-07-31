import itertools

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

array = itertools.permutations(numbers, m)

sorted_array = sorted(array)

for i in sorted_array:
    for j in i:
        print(j, end = ' ')
    print()