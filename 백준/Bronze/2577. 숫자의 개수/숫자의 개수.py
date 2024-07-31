multi = 1
numbers = [0,0,0,0,0,0,0,0,0,0]

while True:
    try:
        num = int(input())
        multi = multi * num
    except EOFError:
        break

for i in str(multi):
    numbers[int(i)] += 1
    

for p in numbers:
    print(p)
