room = input()
numbers = [0,0,0,0,0,0,0,0,0,0]


for i in room:
    numbers[int(i)] += 1

numof = numbers[6] + numbers[9]
sixnine = (numof+1) // 2
numbers[6] = numbers[9] = sixnine


print(max(numbers))