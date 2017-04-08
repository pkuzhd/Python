# -*- coding: utf-8 -*-
ins = input().split(' ')
name, age, sno = ins[0], ins[1], ins[2]
class People:
    def __init__(self, name, age):
        self.name, self.age = name, age
        
    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

class Student(People):
    def __init__(self, name, age, sno):
        self.name, self.age, self.sno = name, age, sno
    
    def getSno(self):
        return self.sno

s = Student(name, age, sno)
print(s.getName() + ' ' + s.getAge()+' '+s.getSno())