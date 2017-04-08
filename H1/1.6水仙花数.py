n = int(input())
def isNarcNum(n):
    sum = 0
    for i in str(n):
        sum += int(i) ** len(str(n))
    if sum == n:
        return True
    else:
        return False

print(isNarcNum(n))