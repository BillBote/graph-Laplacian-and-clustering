import numpy as np
import random


# two parallel lines
x=[]
y=[]
z=[]

a1=[]
b1=[]
c1=[]

# the first line
for i in range(1000):
    a1.append(0)
    b1.append(2)
    c1.append(random.uniform(-3.5,3.5))

x.extend(a1)
y.extend(b1)
z.extend(c1)


a2=[]
b2=[]
c2=[]

# the second line
for i in range(1000):
    a2.append(-2)
    b2.append(1)
    c2.append(random.uniform(-3.5,3.5))

x.extend(a2)
y.extend(b2)
z.extend(c2)

data=[]
for i in range(len(x)):
    data.append([x[i],y[i],z[i]])   


if __name__ == "__main__":

    print(data)
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    ax = plt.subplot(111, projection='3d')
    ax.scatter(x,y,z)
    plt.show()