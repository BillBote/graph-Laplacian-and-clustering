import numpy as np
import random

# data simulation 
# data for a cube

x=[]
y=[]
z=[]


x1=[]
y1=[]
z1=[]

# cube part: range[-3.5,3.5]
for i in range(2000):
    x1.append(random.uniform(-3.5,3.5))
    y1.append(random.uniform(-4,4))
    z1.append(random.uniform(-5,5))

x.extend(x1)
y.extend(y1)
z.extend(z1)


data=[]
for i in range(len(x)):
    data.append([x[i],y[i],z[i]])



if __name__ == '__main__':

    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    ax = plt.subplot(111, projection='3d')
    ax.scatter(x,y,z)
    plt.show()


