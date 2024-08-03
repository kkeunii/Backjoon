word = input()
bang = input()
bang_len = len(bang)
stack = []

for char in word:
    stack.append(char)
    if len(stack) >= bang_len and ''.join(stack[-bang_len:]) == bang:
        del stack[-bang_len:]

result = ''.join(stack)

if result == '':
    print("FRULA")
else:
    print(result)