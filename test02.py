# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 15:04:05 2018

@author: 46980
"""
import math
import numpy as np  
import matplotlib.pyplot as plt  
sum = 0
for x in range(101):
    sum = sum +x
print(sum)
L = ['A','B','C']
for L1 in L:
    print(L1)
n = 0
while n<10:
    n=n+1
    if n%2 == 0:
        continue
    print(n)
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))
def qua(a,b,c):
    x1=(-b-math.sqrt(b*b-4*a*c))/(2*a)
    x2=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    return(x1,x2)
x,y = qua(2,3,1)
print (x,y)
#x=np.linspace(-np.pi,np.pi,256,endpoint=True)  
#C,S=np.cos(x),np.sin(x)  
#plt.plot(x,C)  
#plt.plot(x,S) 
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n*n
    return sum
print(calc(2,4,5))
def person(name,age,**kw):
    print('name',name,'age',age,'other',kw)
person('wangyingying',24)
person('zengyijia',29,city='xiamen')

