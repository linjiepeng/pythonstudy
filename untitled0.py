# -*- coding: utf-8 -*-
"""
Created on Sat Jun  9 14:54:30 2018

@author: 46980
"""
#funcition
def yanghui(max):
    L=[]
    A=[]
    n=0
    while n<max:
        L.append(1)
        A.append(1)
        
        #print(b)
        for x in range(n):
           L[0]=1
           if x>0:
               L[x]=A[x]+A[x-1]
           
        
        print(L)
        for x in range(n):
            A[x]=L[x]
        n=n+1
    
yanghui(10)
list(map(yanghui,[1,2,3]))
from functools import reduce
def fn(x,y):
    return x*10+y
print(reduce(fn,[1,3,5,7,9]))