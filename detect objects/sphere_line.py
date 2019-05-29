"""
Author: Pengfei He
Date: 04/15/2019
Aim: Simulate two objects: one 3-dimensional sphere and one 2-dimensional line
Details: Each objects has 1000 points; sphere with radius 3 and line with length 7; without random error
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

random.seed(20190519)

x=[]
y=[]
z=[]

i=0

while i<500:
    xnew=random.uniform(-3,3)
    ynew=random.uniform(-3,3)
    if xnew**2+ynew**2<9:
        znew=np.sqrt(9-xnew**2-ynew**2)*random.sample([-1,1],1)[0]
        x.append(xnew)
        y.append(ynew)
        z.append(znew)
        i=i+1

x1=[]
y1=[]
z1=[]
for i in range(500):
    xnew=random.uniform(-3.5,3.5)
    x1.append(xnew)
    y1.append(xnew)
    z1.append(-1.5*xnew)

x.extend(x1)
y.extend(y1)
z.extend(z1)

data=[]
for i in range(len(x)):
    data.append([x[i],y[i],z[i]])

