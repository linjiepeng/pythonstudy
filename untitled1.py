# -*- coding: utf-8 -*-
"""
Created on Sat Jun 23 11:54:08 2018

@author: 46980
"""
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    max=min=L[0]
    for key in L:
        if max<= key:
            max=key
        if min>= key:
            min = key
    print(min,max)        
    return (min, max)
  
findMinAndMax([5,4,3,2])     
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[s.lower() for s in L1 if isinstance(s, str)]
print(L2)