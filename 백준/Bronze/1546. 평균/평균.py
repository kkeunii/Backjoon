count = int(input())
num = list(map(int, input().split()))

big = max(num)

numbers = list(map(lambda x: x/big*100, num))

result = 0
for i in numbers:
    result += i

print(result/count)
