# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
"""
from skimage import io
img=io.imread('G:\工作\紧凑型\meiyang2.jpg')
io.imshow(img)
"""

#print ('I LOVE \nWANGYINGYING')
#print (r'''I’m OK
#      Are you OK
#     \\''')
#name = input('pelase enter your name')
#print('hello,',name,',nice to meet you.')
#s1=72
#s2=85
#r=(s2/s1-1)*100
#print('小明成绩提升了：%.1f %%' %r)
enter = True
while enter:
    sg = input("请输入身高：")
    tz = input("请输入体重：")
    sg1=float(sg)
    tz1=float(tz)
    bmi=tz1/(sg1*sg1)
    if bmi <18.5:
        print("BMI指数%.1f 过轻"%bmi)
    elif bmi>=18.5 and bmi<25:
        print("BMI指数%.1f 正常"%bmi)
    elif bmi>=25 and bmi<28:
        print("BMI指数%.1f 过重"%bmi)
    elif bmi>=28 and bmi<32:
        print("BMI指数%.1f 肥胖"%bmi)
    else:
        print("BMI指数%.1f 严重肥胖"%bmi)
    enter1=input("按y继续，按其他任意键退出")
    if enter1 == 'y':
        enter = True
    elif enter1 != 'y':
        enter = False
        
    
        