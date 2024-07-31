import itertools


n, k = map(int, input().split())

result = 1
for i in range(n, n-k, -1):
    result *= i
    
mul = 1

for i in range(1, k+1):
    mul *= i

print(int(result / mul))