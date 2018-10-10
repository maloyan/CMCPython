def rec(n, ans):
    if n == 0:
        return ans
    else:
        ans = ans * 10 + n % 10
        return rec(n//10, ans)
a = int(input())
if rec(a, 0) == a:
    print("YES")
else:
    print("NO")
