n = int(input())
def writeNarcNum(n):
    s = ''
    for i in range(100,n+1):
        sum = 0
        for j in str(i):
            sum += int(j) ** len(str(i))
        if sum == i:
            s += str(i) + '\n'
    return s

print(writeNarcNum(n))