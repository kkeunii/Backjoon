import sys
from collections import deque

result = deque()

def push_front(n):
    result.insert(0, n)

def push_back(n):
    result.append(n)

def pop_front():
    if len(result) == 0:
        return(-1)
    else:
        return result.popleft()
    
def pop_back():
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
    if order[0] == 'push_front':
        push_front(int(order[1]))
    elif order[0] == 'push_back':
        push_back(int(order[1]))
    elif order[0] == 'pop_front':
        print(pop_front())
    elif order[0] == 'pop_back':
        print(pop_back())
    elif order[0] == 'size':
        print(size())
    elif order[0] == 'empty':
        print(empty())
    elif order[0] == 'front':
        print(front())
    elif order[0] == 'back':
        print(back())