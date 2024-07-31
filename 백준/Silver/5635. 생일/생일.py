birth = {}
count = int(input())
while True:
    try:
        name = input().split()

        if len(name[1]) == 1:
            name1 = "0" + name[1]
        else:
            name1 = name[1]
        if len(name[2]) == 1:
            name2 = "0" + name[2]
        else:
            name2 = name[2]
        
        birth[name[0]] = (name[3] + name2 + name1)
    except EOFError:
        break

print(max(birth, key=birth.__getitem__))
print(min(birth, key=birth.__getitem__))
