import fileinput
d = dict()
for line in fileinput.input():
    for i in line.split():
        if i in d:
            d[i] += 1
        else:
            d[i] = 0
s = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]
if len(s) == 0:
    print("---")
elif len(s) == 1 or s[0][1] > s[1][1]:
    print(s[0][0])
else:
    print("---")
