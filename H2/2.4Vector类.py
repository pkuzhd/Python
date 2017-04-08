# -*- coding: utf-8 -*-
class Vector3:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector3(x, y, z)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        return Vector3(x, y, z)

    def __mul__(self, n):
        x = self.x * n
        y = self.y * n
        z = self.z * n
        return Vector3(x, y, z)

    def __truediv__(self, n):
        x = self.x / n
        y = self.y / n
        z = self.z / n
        return Vector3(x, y, z)

    def __str__(self):
        return "(%s,%s,%s)" % (self.x, self.y, self.z)

data=input().split(' ')
s1,s2,m,n=eval(data[0]),eval(data[1]),int(data[2]),int(data[3])
v1=Vector3(s1[0],s1[1],s1[2])
v2=Vector3(s2[0],s2[1],s2[2])
print(str(v1+v2)+' '+str(v1-v2)+' '+str(v1*m)+' '+str(v1/n))