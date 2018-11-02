from collections import deque

a = eval(input())
p = [0] * len(a)

queue = deque([0])
ans = False
while queue:
    cur_ind = queue.popleft()
    if cur_ind == len(a) - 1:
        ans = True
        break
    p[cur_ind] == 1
    left = cur_ind - 1
    right = cur_ind + a[cur_ind]
    if right < len(a) and p[right] == 0:
        queue.append(right)
        p[right] = 1
    if left > 0 and p[left] == 0:
        queue.append(left)
        p[left] = 1

if ans:
    print("YES")
else:
    print("NO")
