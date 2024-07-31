import sys
from collections import deque

result = deque()

def push(n):
    result.append(n)

def pop():
    if len(result) == 0:
        return(-1)
    else:
        return result.popleft()
    
def size():
    return len(result)

def empty():
    if len(result) == 0:
        return(1)
    else:
        return(0)

def front():
    if len(result) == 0:
        return(-1)
    else:
        return result[0]

def back():
    if len(result) == 0:
        return(-1)
    else:
        return result[-1]

count = int(sys.stdin.readline())

for _ in range(count):
    order = sys.stdin.readline().split()
    if order[0] == 'push':
        push(int(order[1]))
    elif order[0] == 'pop':
        print(pop())
    elif order[0] == 'size':
        print(size())
    elif order[0] == 'empty':
        print(empty())
    elif order[0] == 'front':
        print(front())
    elif order[0] == 'back':
        print(back())