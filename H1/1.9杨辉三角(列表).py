n = int(input())
def printTri(n):
    s = ""
    if n == 1:
        s ='1'
    else:
        p = [[1], [1, 1]]  #创建列表
        s = '1\n1 1\n'
        for i in range(2,n):
            p.append(['1'])
            for j in range(0,i-1):
                p[i].append(str(int(p[i-1][j]) + int(p[i-1][j+1])))
            p[i].append('1')
            s = s + ' '.join(p[i]) + '\n'
    return s

print(printTri(n))
