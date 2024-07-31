num = int(input())
mul = 1
count = 0

for i in range(1, num+1):
    mul = mul * i

result = str(mul)

for q in result[::-1]:

    if q == "0":
        count += 1
    elif q != "0":
        break

print(count)