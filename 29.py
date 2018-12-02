from collections import Counter

class DefCounter(Counter):
    def __init__(self, *arg, missing=-1, **argn):    
        if argn:
            self.string = Counter(argn)
        else:
            self.string = Counter(*arg)
        self.missing = missing

    def __missing__(self,key):
        if self.string[key]:
            return self.string[key]
        return self.missing

    def __setitem__(self, key, value):
        self.string[key] = value

    def __str__(self):
        return f'DefCounter({dict(self.string)})'

#A = DefCounter(a=2,b=3,c=8,missing=2)
#print(A["a"], A["c"], A["f"])
#A = DefCounter(range(10))
#print(A)
#print(A[5])
#A = DefCounter("QWEqweQWEqweQWE", missing=-10)
#print(A)
#print(A["Z"])
#A["P"] += 5
#print(A)
