def squares(x, y, *arg):
    a = []
    for i in range(y):
        raw = []
        for j in range(x):
            raw.append('.')
        a.append(raw)

    for k in range(len(arg)):
        X = arg[k][0]
        Y = arg[k][1]
        for i in range(arg[k][2]):
            for j in range(arg[k][2]):
                a[Y+i][X+j] = arg[k][3]

    for i in range(y):
        print(''.join(a[i]))
