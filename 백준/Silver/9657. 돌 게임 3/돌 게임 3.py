count = int(input())

sk = [1, 3, 4, 5, 6]
cy = [2, 7]
i = 8

while i <= count:
    win = 0
    if i-4 in sk:
        win += 1
    if i-3 in sk:
        win += 1
    if i-1 in sk:
        win += 1

    if win == 3:
        cy.append(i)
    else:
        sk.append(i)
    i += 1
        
if count in sk:
    print("SK")
else:
    print("CY")
