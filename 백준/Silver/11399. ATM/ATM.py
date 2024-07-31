number = int(input())
time = list(map(int, input().split()))

time.sort()
sum = 0
for i in range(0, number):
    sum = sum + time[i]*(number-i)

print(sum)