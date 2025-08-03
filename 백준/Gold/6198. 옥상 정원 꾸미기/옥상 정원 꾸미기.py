num = int(input())
building = []
for i in range(num):
    building.append(int(input()))

answer = 0
stack = [] 


for i in range(num):
    while stack and building[i] >= stack[-1] :
        stack.pop()

    answer += len(stack)
    stack.append(building[i])
    

print(answer)
