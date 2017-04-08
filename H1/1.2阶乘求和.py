n = int(input())
def factorailSum(n):
    s = 0
    for i in range(1,n+1):
        m = 1 #m用来记录j的阶乘
        for j in range(1,i+1):
            m *= j
        s += m
    return s

print(factorailSum(n))