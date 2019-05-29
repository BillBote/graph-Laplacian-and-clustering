"""
Author: Pengfei He
Date: 05/01/2019
Aim: Simulate two 2-dimensional lines
Details: two interact lines both with length 7 and no random error
"""
import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

random.seed(20190519)
d=[]
e=[]
f=[]

for i in range(500):
    dnew=random.uniform(-3,3)
    d.append(dnew)
    e.append(-dnew)
    f.append(0)
    
d1=[]
e1=[]
f1=[]

for i in range(500):
    dnew=random.uniform(-3,3)
    d1.append(dnew)
    e1.append(dnew)
    f1.append(0)

d.extend(d1)
e.extend(e1)
f.extend(f1)


data=[]
for i in range(len(d)):
    data.append([d[i],e[i],f[i]]) 