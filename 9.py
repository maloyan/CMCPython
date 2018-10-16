def moar(a, b, n):
    x, y = 0, 0
    for i in a:
        if i % n == 0:
            x = x + 1
    for i in b:
        if i % n == 0:
            y = y + 1
    if x > y:
        return True
    else:
        return False

