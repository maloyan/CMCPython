a = input()
b = input()

ans = 0
j = 0
test = 0
if len(a) >= len(b):
    for i in range(len(a)):
        if a[i] == b[j] or b[j] == '@':
            ans += 1
            j += 1
        else:
            ans = 0
            j = 0
        if ans == len(b):
            test = 1
            print(i - len(b) + 1)
            break
    if test == 0:
            print(-1)
else:
    print(-1)
