numbers = []

while True:
    try:
        num = int(input())
        numbers.append(num)
    except EOFError:
        break
left = []
for i in numbers:
    left.append(i%42)
    
number = list(set(left))

print(len(number))
