count = int(input())

strings = []

for i in range(count):
    user = input().split()
    strings.append(user)

for i in strings:
    for p in range(len(i[1])):
        print(i[1][p] * int(i[0]), end="")
    print()
