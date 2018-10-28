def f(cur_pos, arr):
    print(cur_pos)
    if cur_pos == 0:
        return True
    else:
        b = False
        for i in range(len(arr)):
            if i - arr[i] == cur_pos or arr[i] + i == cur_pos:
                b = b or f(i, arr)
        return b
a = eval(input())
if f(-1, a):
    print("YES")
else:
    print("NO")
 
