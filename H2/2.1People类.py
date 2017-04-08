# -*- coding: utf-8 -*-
ins = input().split(' ')
name,age = ins[0],int(ins[1])
class People:
    def __init__(self, name, age):
        self.name, self.age = name, age
        
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
p = People(name, age)
print(p.getName()+' '+str(p.getAge()))