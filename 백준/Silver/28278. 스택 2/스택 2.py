import sys

result = []

def push(n):
    result.append(n)

def pop():
    if len(result) == 0:
        return(-1)
    else:
        return result.pop()

def size():
    return len(result)

def empty():
    if len(result) == 0:
        return(1)
    else:
        return(0)

def top():
    if len(result) == 0:
        return(-1)
    else:
        return result[-1]

count = int(sys.stdin.readline())

for _ in range(count):
    order = sys.stdin.readline().split()
    if order[0] == '1':
        push(int(order[1]))
    elif order[0] == '2':
        print(pop())
    elif order[0] == '3':
        print(size())
    elif order[0] == '4':
        print(empty())
    elif order[0] == '5':
        print(top())