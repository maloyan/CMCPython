import re

a = re.findall(r"[\w']+|[.,!?;]", input())
b = re.findall(r"[\w']+|[.,!?;]", input())
a = [i.lower() for i in a]
b = [i.lower() for i in b]

if len(a) == 1 and len(b) == 1:
    print(a == b)
else:
    print(sorted(a) == sorted(b))
