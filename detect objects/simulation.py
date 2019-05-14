import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x=[]
y=[]
z=[]

"""
while i<1000:
    xnew=random.uniform(-3,3)
    ynew=random.uniform(-3,3)
    if xnew**2+ynew**2<9:
        znew=np.sqrt(9-xnew**2-ynew**2)*random.sample([-1,1],1)[0]
        x.append(xnew+random.gauss(0,0.1))
        y.append(ynew+random.gauss(0,0.1))
        z.append(znew+random.gauss(0,0.1))
        i=i+1


x1=[]
y1=[]
z1=[]
for i in range(1000):
    xnew=random.uniform(-3.5,3.5)
    x1.append(xnew+random.gauss(0,0.2))
    y1.append(xnew+random.gauss(0,0.2))
    z1.append(-1.5*xnew+random.gauss(0,0.2))
x.extend(x1)
y.extend(y1)
z.extend(z1)


data=[]
for i in range(len(x)):
    data.append([x[i],y[i],z[i]])

print(data)
ax = plt.subplot(111, projection='3d')
ax.scatter(x,y,z)
plt.show()
"""

x=[]
y=[]
z=[]

for i in range(1000):
    x.append(random.uniform(-3,3))
    y.append(random.uniform(-3,3))
    z.append(random.gauss(0,0.06))

x1=[]
y1=[]
z1=[]

for i in range(1000):
    x1.append(1+random.gauss(0,0.01))
    y1.append(2+random.gauss(0,0.01))
    z1.append(random.uniform(-3.5,3.5))

x.extend(x1)
y.extend(y1)
z.extend(z1)


x2=[]
y2=[]
z2=[]

for i in range(1000):
    x2.append(-2+random.gauss(0,0.01))
    y2.append(-1+random.gauss(0,0.01))
    z2.append(random.uniform(-3.5,3.5))

x.extend(x2)
y.extend(y2)
z.extend(z2)

data=[]
for i in range(len(x)):
    data.append([x[i],y[i],z[i]])   

