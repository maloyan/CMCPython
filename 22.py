import fileinput
d = dict()
for line in fileinput.input():
    a, b = map(int, line.split(','))
    if a in d:
        d[a].add(b)
    else:
        d[a] = {a, b}
    if b in d:
        d[b].add(a)
    else:
        d[b] = {a, b}
    if a == 0 and b == 0:
        break
for i in d:
    if len(d) == len(d[i]):
        print(i, end = " ")
    
