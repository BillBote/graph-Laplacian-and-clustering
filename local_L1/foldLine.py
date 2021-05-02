import numpy as np
import random

# data simulation 
# fold line

x=[]
y=[]
z=[]

x3=[]
y3=[]
z3=[]

# line part2: 
for t in np.arange(-1,1,0.005):
    x3.append(t)
    y3.append(8-2*t)
    z3.append(t)

x.extend(x3)
y.extend(y3)
z.extend(z3)

x1=[]
y1=[]
z1=[]

# line part1: range[-3.5,3.5]
for t in np.arange(-6,6,0.012):
    x1.append(1)
    y1.append(t)
    z1.append(1)

x.extend(x1)
y.extend(y1)
z.extend(z1)

x2=[]
y2=[]
z2=[]

# line part2: 
for t in np.arange(1,3,0.005):
    x2.append(t)
    y2.append(-4-2*t)
    z2.append(t)

x.extend(x2)
y.extend(y2)
z.extend(z2)



data=[]
for i in range(len(x)):
    data.append([x[i],y[i],z[i]])



if __name__ == '__main__':

    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    ax = plt.subplot(111, projection='3d')
    ax.scatter(x,y,z)
    plt.show()


