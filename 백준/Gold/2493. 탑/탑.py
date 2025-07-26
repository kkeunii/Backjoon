num = int(input())
top = list(map(int, input().split()))
answer = [0] * num
stack = [] 


for i in range(num - 1, -1, -1):
    while stack and top[i] > top[stack[-1]]:
        idx = stack.pop()
        answer[idx] = i + 1 
    stack.append(i)

print(*answer)