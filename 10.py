def check(n):
    x = 2
    while x * x <= n:
        if n % x == 0:
            return False
        x = x + 1
    return True
        

a = int(input())
while check(a) == False:
    a = a - 1
print(a)
