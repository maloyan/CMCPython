a = int(input())
x, y, z = 2, 4, 7

for i in range(3, a):
    x, y, z = y, z, x + y + z
print(z)
