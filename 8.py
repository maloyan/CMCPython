def gcd(a,b): 
    if(b==0): 
        return a 
    else: 
        return gcd(b,a%b)

a, b = map(int, input().split(", "))

if a < b:
    x = gcd(a, b)
    print(str(int(a / x))+"/"+str(int(b / x)))
elif a%b == 0:
    print(int(a/b))
else:
    num = a//b
    a = a % b
    x = gcd(a, b)
    print(str(num), str(int(a / x))+"/"+str(int(b / x)))
