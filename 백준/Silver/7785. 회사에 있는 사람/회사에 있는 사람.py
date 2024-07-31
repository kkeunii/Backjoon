people = int(input())
current = set()

for i in range(people):
    user = input().split()
    name, action = user[0], user[1]

    if action == "enter":
        current.add(name)
    else:
        current.remove(name)

for name in sorted(current, reverse=True):
    print(name)