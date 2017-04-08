s = input()
def en2num(s):
    n = ''
    dic1 = {'zero':'0',
            'one':'1', 
            'two':'2', 
            'three':'3', 
            'four':'4', 
            'five':'5', 
            'six':'6', 
            'seven':'7',
            'eight':'8',
            'nine':'9'}  #创建字典
    for i in s.split('-'):
        n = n + dic1[i]   #把英语和数字一一对应
    return n
    
print(en2num(s))
