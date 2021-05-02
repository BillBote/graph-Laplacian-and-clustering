import numpy as np
import random


# data for one lines and one plane, vertical

x=[]
y=[]
z=[]

x1=[]
y1=[]
z1=[]

# plane part:
ynew=np.arange(-3,3,0.006)
for i in range(len(ynew)):
    x1.append(0)
    y1.append(ynew[i])
    z1.append(random.uniform(-3.5,3.5))

x.extend(x1)
y.extend(y1)
z.extend(z1)


x2=[]
y2=[]
z2=[]

# line part

xnew=np.arange(-3.5,3.5,0.007)
for i in range(len(xnew)):
    x2.append(xnew[i])
    y2.append(0)
    z2.append(0)

x.extend(x2)
y.extend(y2)
z.extend(z2)

data=[]
for i in range(len(x)):
    data.append([x[i],y[i],z[i]])   


if __name__ == "__main__":

    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    ax = plt.subplot(111, projection='3d')
    ax.scatter(x,y,z)
    plt.show()