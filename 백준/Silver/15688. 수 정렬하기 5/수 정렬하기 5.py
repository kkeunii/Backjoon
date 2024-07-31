import sys

input = sys.stdin.read
numbers = list(map(int, input().split()))

numbers = numbers[1:]
sorted_numbers = sorted(numbers)

for number in sorted_numbers:
    print(number)