count = int(input())
date = list(map(int, input().split()))

date.sort(reverse = True)

a=count
dates = []

for i in range(a):
    new_value = date[i] - (a - i)
    dates.append(new_value)

most = max(dates)

print(most + count + 2)
