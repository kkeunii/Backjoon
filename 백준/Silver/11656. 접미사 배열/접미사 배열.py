word = input()
words = []

for i in range(0, len(word)):
    words.append(word[i:])


words.sort()
for i in words:
    print(i)
