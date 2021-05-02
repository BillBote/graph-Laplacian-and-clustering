import numpy as np
import random

# data simulation 
# data1 for a Sphere and a circle

x=[]
y=[]
z=[]


# sphere part: radius=3
i=0
while i<1000:
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

# circle part: radius=3
for i in range(1000):
    xnew=random.uniform(-3,3)
    ynew=np.sqrt(9-xnew**2)*random.sample([-1,1],1)[0]+2
    x1.append(xnew-1)
    y1.append(1)
    z1.append(ynew)

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
