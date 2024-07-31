money = int(input())

cut5 = money // 5

if money == 1 or money == 3:
    result = -1
elif (money % 5) % 2 == 0:
    cut2 = (money - (cut5*5)) // 2
    result = cut5 + cut2
else:
    cut2 = (money - (cut5-1)*5) // 2
    result = cut5 -1 + cut2

print(result)
