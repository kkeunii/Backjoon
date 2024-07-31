height = []
sum = 0
flag = False

for i in range(9):
    value = int(input())
    height.append(value)
    sum = sum + int(height[i])

for p in range(0, 9):
    for q in range(0, 9):
        result = sum
        if p == q:
            continue
        result = result - int(height[p]) - int(height[q])

        if result == 100:
            flag = True
            a = height[p]
            b = height[q]
            height.remove(a)
            height.remove(b)
        if flag == True:
            break
    if flag == True:
            break

height.sort()
for i in range(7):
    print(height[i])