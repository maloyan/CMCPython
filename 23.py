def toint(f):
    def newfun(*args):
        new = []
        for i in args:
            if type(i) is float:
                new.append(int(i))
            else:
                new.append(i)
        res = f(*new)
        if type(res) is float:
            res = int(res)
        return res
    return newfun

#@toint
#def root(x):
#    return x**0.5
#print(root(11.8))
