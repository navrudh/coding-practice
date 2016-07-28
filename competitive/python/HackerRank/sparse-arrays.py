"""
 Data Structures > Arrays > Sparse Arrays

"""

strings = [input() for i in range(int(input()))]

for i in range(int(input())):
    query = input()
    count = 0
    for stri in strings:
        if stri == query:
            count += 1
    print(count)
