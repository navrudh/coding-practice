"""
 Data Structures > Arrays > Left Rotation

"""
n, d = [int(x) for x in input().split()]
arr = [arr for arr in input().split()]

print( ' '.join(arr[d % n:]) + ' ' + ' '.join(arr[:(d % n)]) )
