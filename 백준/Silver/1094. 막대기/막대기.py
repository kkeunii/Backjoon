length = int(input())
a = length
sumof = 0
start = 64
count = 0

while sumof != a:
    if start == 1:
        sumof = sumof + start
        count +=1
    elif length < start:
        start = start //2
    else:
        sumof = sumof + start
        count += 1
        length = length-start
        start = start // 2

print(count)