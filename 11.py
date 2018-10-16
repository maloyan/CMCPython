x = list(map(int, input().split(',')))

for i in range(len(x)):
    if i == 0:
        max1 = x[i]
    elif max1 < x[i]:
        max1 = x[i]
max2 = None
for i in range(len(x)):
    if (max2 == None or max2 < x[i]) and x[i] < max1:
        max2 = x[i]
if max2 == None:
    print("NO")
else:
    print(max2)
