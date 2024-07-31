def is_matched(expr):
    lefty = '('
    righty = ')'

    s = []
    for c in expr:
        if c == lefty:
            s.append(c)
        elif c == righty:
            if len(s) == 0:
                return "NO"
            if s[-1] == lefty:
                s.pop()
    if len(s) != 0:
        return "NO"
    
    return "YES"

count = int(input())
for i in range(count):
    expr = input()
    print(is_matched(expr))