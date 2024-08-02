from itertools import combinations

n, m = map(int,input().split())

card = list(map(int, input().split()))
numbers = list(combinations(card, 3))

total = 0

for i in numbers:
    if sum(i) <= m:
        total = max(total, sum(i))
        
print(total)
