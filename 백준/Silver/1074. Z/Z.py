n, x, y = map(int,input().split())

def z_recursion(n, x, y, sum):
    length = 2**n
    a = length//2
    if n == 1:
        return sum + x*2 + y
    else: 
        if x < a and y < a:      #1사분면
            return z_recursion(n-1, x, y,  sum+0)
        elif x < a and y >= a:      #2사분면
            return z_recursion(n-1, x, y-a, sum + a**2)
        elif x >= a and y < a:       #3사분면
            return z_recursion(n-1, x-a, y, sum + a**2 * 2)
        elif x >= a and y >= a:       #4사분면
            return z_recursion(n-1, x-a, y-a, sum + a**2 * 3)
            
print(z_recursion(n, x, y, 0))