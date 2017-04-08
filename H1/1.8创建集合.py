s1 = input()
s2 = input()
def getUnion(s1,s2):
    set1 = set(list(s1))#创建集合1
    set2 = set(list(s2))#创建集合2
    return set1 | set2  #求并集

print(sorted(getUnion(s1,s2)))