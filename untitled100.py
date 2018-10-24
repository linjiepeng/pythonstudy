# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 15:35:45 2018

@author: 46980
"""
import random
temp = input("猜个数字吧:")
guess = int(temp)

bb = random.randint(0,100)
#print (bb)
enter = True
while enter:
  if guess == bb:
      print ("恭喜回答正确！" )
      enter = False
  else:
      #print('you are wrong,the right number is %d' % bb)
      if guess < bb:
          asd = '小'
      else:
          asd = '大'
      print('你猜的数%s了,请重新猜吧' % asd)
    
#print("Game Over")