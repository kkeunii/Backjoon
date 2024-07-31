count = int(input())
students = []

while True:
    try:
        student = list(map(int, input().split()))
        students.append(student)
    except EOFError:
        break

for i in students:
    num = i[0]
    score = i[1:]
    scores = sorted(score, reverse = True)
    max_score = max(score)
    min_score = min(score)

    sub = []
    for p in range(num-1):
        sub.append(scores[p]-scores[p+1])

    
    print("Class", students.index(i)+1)
    print(f"Max {max_score}, Min {min_score}, Largest gap {max(sub)}", end="\n")
