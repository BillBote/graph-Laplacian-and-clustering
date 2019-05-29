"""
Author: Pengfei He
Date: 04/20/2019
Aim: Simulate three objects: one plane and two parallel lines
Details: Each objects contains 1000 points; plane [-3,3]*[-3,3]; lines with length 7; without random error
"""



from numpy import *
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


random.seed(20190519)

a=[]
b=[]
c=[]

for i in range(1000):
    a.append(random.uniform(-3,3))
    b.append(random.uniform(-3,3))
    c.append(0)
    
a1=[]
b1=[]
c1=[]

for i in range(1000):
    a1.append(1)
    b1.append(2)
    c1.append(random.uniform(-3.5,3.5))

a.extend(a1)
b.extend(b1)
c.extend(c1)


a2=[]
b2=[]
c2=[]

for i in range(1000):
    a2.append(-2)
    b2.append(-1)
    c2.append(random.uniform(-3.5,3.5))

a.extend(a2)
b.extend(b2)
c.extend(c2)

data=[]
for i in range(len(a)):
    data.append([a[i],b[i],c[i]])   