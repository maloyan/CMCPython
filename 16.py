from collections import deque

def LookSay():
    deq = deque([1, 0])
    i, count_of_number = 1, 0
    while 1:
        number = deq.popleft()
        if number != 0 :
            yield number

        if number == i :
            count_of_number += 1
        else:
            if i != 0:
                deq.append(count_of_number)
            deq.append(i)
            count_of_number, i = 1, number


