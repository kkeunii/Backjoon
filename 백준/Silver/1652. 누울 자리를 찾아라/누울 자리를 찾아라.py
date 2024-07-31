size = int(input())
room = []

while True:
    try:
        row = input()
        room.append(row)
    except EOFError:
        break

    
row = 0
col = 0

for i in room:
    count = 0
    for p in i:
        if p == ".":
            count += 1
        elif p == "X":
            count = 0
            
        if count == 2:
            row += 1


for i in range(0, size):
    count = 0
    for p in range(0, size):
        if room[p][i] == ".":
            count += 1
        elif room[p][i] == "X":
            count = 0
            
        if count == 2:
            col += 1
    

print(row, col)
