def generator(a):
    yield -a
    yield str(a)
    yield abs(a)//10%10
