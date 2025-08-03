num = int(input())
numbers = list(map(int, input().split()))
answer = [0] * num
stack = [] 


for i in range(num - 1, -1, -1):
    while stack and numbers[i] >= stack[-1]:
        stack.pop()
    answer[i] = stack[-1] if stack else -1
    stack.append(numbers[i])

print(*answer)
