# -*- coding: utf-8 -*-
dct=eval(input())
class Xdict(dict):
    def getKeys(self, val):
        s = []
        for key in self:
            if self[key] == val:
                s.append(key)
        return s

print(' '.join(sorted(list(map(str,Xdict(dct).getKeys('a'))))))