ablist = ["A"]
count = int(input())

acount = 1
bcount = 0

for i in range(0, count):
    a = acount
    b = bcount
    bcount = b + a
    acount = b

    
print(acount, bcount, end=" ")
