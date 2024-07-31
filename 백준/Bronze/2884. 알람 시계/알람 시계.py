h, m = map(int, input().split())

if m - 45 >= 0:
    m = m - 45
elif m - 45 < 0 and h != 0:
    h = h - 1
    m = m + 15
else:
    h = 23
    m = m + 15

print(h,m, end="")
