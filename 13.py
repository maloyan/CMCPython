import math
def numeric_compare(x):
    return math.sin(x) 
print(sorted(eval(input()), key=numeric_compare))
