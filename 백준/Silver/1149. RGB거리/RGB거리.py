num = int(input())
paint = []

while True:
    try:
        price = list(map(int, input().split()))
        paint.append(price)
    except EOFError:
        break
    
resultdp = []
for i in range(0, len(paint)):
    if i == 0:
        resultdp.append(paint[0])

    else:
        a = []
        for p in range(0, 3):
            new = paint[i][p] + min(resultdp[i-1][:p] + resultdp[i-1][p+1:])
            a.append(new)
        resultdp.append(a)

print(min(resultdp[-1]))