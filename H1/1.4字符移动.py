s = input()
n = int(input())
def reverse(s,n):
    length = len(s)
    n =  n % length
    return s[-n:] + s[:-n]
    
print(reverse(s,n))