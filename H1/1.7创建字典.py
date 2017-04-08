keys = eval(input())
values = eval(input())
def generateDict(keys,values):
    dict1 = {}
    n = len(keys)
    for i in range(n):
        dict1[keys[i]] = values[i]   #把keys和values一一对应
    return dict1
    
print(generateDict(keys,values))
