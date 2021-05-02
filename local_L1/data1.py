import numpy as np
import random

# data simulation 
# data1 for a Sphere and a Line

x=[]
y=[]
z=[]


# sphere part: radius=3
x1=[]
y1=[]
z1=[]
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


x2=[]
y2=[]
z2=[]

# line part: range[-3.5,3.5]
xnew=np.arange(-3.5,3.5,0.007)
for i in range(len(xnew)):
    x2.append(xnew[i])
    y2.append(xnew[i])
    z2.append(-1.5*xnew[i])

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


