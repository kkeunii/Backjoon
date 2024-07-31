while True:
    try:
        num = list(map(int, input().split()))
        c = max(num)
        del num[num.index(c)]
        if c == 0 and num[0] == 0 and num[1] == 0:
            break
        elif c**2 == num[0]**2 + num[1]**2:
            print("right")
        else:
            print("wrong")
    except EOFError:
        break
