import numpy as np
import random

# data simulation 
# a Line

x=[]
y=[]
z=[]


x1=[]
y1=[]
z1=[]

# line part: range[-3.5,3.5]
for i in range(1000):
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



if __name__ == '__main__':

    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    ax = plt.subplot(111, projection='3d')
    ax.scatter(x,y,z)
    plt.show()


