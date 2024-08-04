import sys
input = sys.stdin.read


data = input().split()

n = int(data[0])
m = int(data[1])


numbers = list(map(int, data[2:n+2]))


prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + numbers[i - 1]


index = n + 2
output = []

for _ in range(m):
    a = int(data[index])
    b = int(data[index + 1])

    sum1 = prefix_sum[b] - prefix_sum[a - 1]
    output.append(str(sum1))
    index += 2


sys.stdout.write("\n".join(output) + "\n")
