ascending = [1, 2, 3, 4, 5, 6, 7, 8]
descending = [8, 7, 6, 5, 4, 3, 2, 1]

user_input = list(map(int, input().split()))

if user_input == ascending:
    print("ascending")
elif user_input == descending:
    print("descending")
else:
    print("mixed")
