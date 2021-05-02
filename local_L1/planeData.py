import numpy as np
import random


# data one plane

x=[]
y=[]
z=[]

a1=[]
b1=[]
c1=[]

# plane part:
for i in range(1000):
    a1.append(0)
    b1.append(random.uniform(-3.5,3.5))
    c1.append(random.uniform(-3.5,3.5))

x.extend(a1)
y.extend(b1)
z.extend(c1)

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

    