import fileinput

ans = None
for a in fileinput.input():
    for i in a.split():
        if i.isnumeric():
            if ans == None:
                ans = int(i)
            elif ans < int(i):
                ans = int(i)
        if i[0] == '-':
            if i[1:].isnumeric():
                if ans == None:
                    ans = int(i)
                elif ans < int(i):
                    ans = int(i)
print(ans)
