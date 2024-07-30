import sys

count = int(sys.stdin.readline())

number = []
for i in range(count):
    num = int(sys.stdin.readline())
    number.append(num)

number.sort(reverse = True)
print(*number, sep='\n')
