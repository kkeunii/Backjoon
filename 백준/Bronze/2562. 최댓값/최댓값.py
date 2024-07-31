numbers = []

for i in range(9):
    num = int(input())
    numbers.append(num)

result = max(numbers)
print(result, numbers.index(result)+1)