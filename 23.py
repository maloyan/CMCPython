def toint(*args):
    print(args)
#   a = []
#   for i in range(len(args)):
#       a.append(int(args[i]))
#   res = int(f(*a))
#   return res

@toint
def root(x):
    return x**0.5
print(root(11.8))
