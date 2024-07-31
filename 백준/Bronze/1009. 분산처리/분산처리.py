def last_digit(a, b):
    # a의 마지막 자릿수만 중요하다.
    a = a % 10
    
    # a의 마지막 자릿수에 따라 패턴이 결정됨
    if a == 0:
        return 10
    elif a == 1:
        return 1
    elif a == 2:
        pattern = [2, 4, 8, 6]
    elif a == 3:
        pattern = [3, 9, 7, 1]
    elif a == 4:
        pattern = [4, 6]
    elif a == 5:
        return 5
    elif a == 6:
        return 6
    elif a == 7:
        pattern = [7, 9, 3, 1]
    elif a == 8:
        pattern = [8, 4, 2, 6]
    elif a == 9:
        pattern = [9, 1]
    
    # 패턴의 길이
    pattern_len = len(pattern)
    
    # b-1의 나머지를 패턴 길이로 나눠 패턴의 인덱스를 결정
    return pattern[(b - 1) % pattern_len]

# 테스트 케이스 입력
t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(last_digit(a, b))
