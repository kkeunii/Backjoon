scores = []

while True:
    try:
        score = int(input())
        scores.append(score)
    except EOFError:
        break

scores_sort = sorted(scores, reverse = True)
result = 0
real = []
for i in range(0, 5):
    real.append(scores_sort[i])
    result = result + scores_sort[i]

print(result)
for i in scores:
    if i in real:
        print(scores.index(i)+1, end=" ")
