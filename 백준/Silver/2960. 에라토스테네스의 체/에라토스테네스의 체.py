def isprime():
    n, k = map(int, input().split())
    prime = []
    count = 0
    for i in range(2, n+1):
        prime.append(i)
    while count != k:
        p = prime[0]
        b = prime[-1]
        for q in range(1, (b//p) + 1):
            if p*q in prime and count != k:
                a = prime.index(p*q)
                result = prime[a]
                del prime[a]
                count = count + 1
            elif count == k:
                break
    return result

print(isprime())