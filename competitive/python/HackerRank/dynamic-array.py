"""
 Data Structures > Arrays > Dynamic Array

"""

n, q = [int(x) for x in input().split()]
s = [[] for i in range(n)]
last = 0

for i in range(q):
    typ, x, y = [int(x) for x in input().split()]
    
    if typ == 1:
        s[(x ^ last) % n].append(y)

    if typ == 2:
        last = s[(x ^ last) % n][y % len(s[(x ^ last) % n])]
        print(last)
