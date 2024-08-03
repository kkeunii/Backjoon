count = int(input())

cy = [1, 3]
sk = [2, 4, 5, 6]
i = 7

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
