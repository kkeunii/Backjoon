import math

def common_divider(a, b):
    while b:
        a, b = b, a % b
    return a

def common_multiple(a, b):
    return a * b // common_divider(a, b)

a, b = map(int, input().split())
result = common_multiple(a, b)

print(result)