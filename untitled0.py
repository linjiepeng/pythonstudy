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
        if L is None:
            L=[]
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
import math

def move(n,a,b,c):
    if n==1:
        print(a,'->',c)
        
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
        
move(2,'A','B','C')
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    print(s)
trim('  asd  ')
