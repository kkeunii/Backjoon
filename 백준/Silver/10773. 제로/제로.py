sum = 0
number = []
count = int(input())
while True:
    try:
        num = int(input())
        if num == 0:
            sum -= number[-1]
            number.pop()
        else:
            number.append(num)
            sum += num
    except EOFError:
        break

print(sum)
