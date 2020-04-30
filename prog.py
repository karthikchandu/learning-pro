# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 23:18:46 2020

@author: KARTHIK
"""

a = [0,3,1,5]
b = [4,2,10,6]
c = []
d = []
for i in range(len(a)):
    if a[i]<b[i]:
        c.append(a[i])
        print(c)
    else:
       d.append(b[i])
       print(d)

#print(min(val) for val in zip(a,b))
#print(max(val) for val in zip(a,b))