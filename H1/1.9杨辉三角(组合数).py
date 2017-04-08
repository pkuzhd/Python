n = int(input())
def printTri(n):
    s = ""
    for i in range(0,n):
        s += '1'
        for j in range(1,i+1):
            sij = 1
            for k in range(i-j+1,i+1):
                sij = sij * k
            for k in range(i-j+1,i+1):
                sij = sij / (i - k + 1)
            s += ' %d'%(sij)
        s += '\n'
    return s
    
print(printTri(n))