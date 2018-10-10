def rec(x, y, r):
    a, b = map(int, input().split(','))
    if a == 0 and b == 0:
        return True
    if ((x - a)**2 + (y - b)**2) <= r*r:
        return True and rec(x, y, r)
    else:
        return False

x, y, r = map(int, input().split(','))
if rec(x, y, r):
    print("YES")
else:
    print("NO")
