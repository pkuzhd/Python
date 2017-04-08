import sys  
y, m = map(int, sys.stdin.readline().split())
def getDays(y,m):
    n = 0
    if m in [1, 3, 5, 7, 8, 10, 12]:
        n = 31
    elif m == 2:
        if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            n = 29
        else:
            n = 28
    else:
        n = 30
    return n

print(getDays(y,m))