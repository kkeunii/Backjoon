num = int(input())
cards = []

for i in range(1, num+1):
    cards.append(i)


while len(cards) != 1:
    print(cards[0], end=" ")
    cards.pop(0)
    cards.append(cards[0])
    cards.pop(0)
    
print(cards[0])
    