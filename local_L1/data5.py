import numpy as np
import random

# a circle and a line
x=[]
y=[]

# circle part
i=0
while i<100:
    xnew=random.uniform(-3,3)
    ynew=np.sqrt(9-xnew**2)*random.sample([-1,1],1)[0]
    x.append(xnew)
    y.append(ynew)
    i=i+1



x1=[]
y1=[]

# line part
for i in range(100):
    xnew=random.uniform(-3.5,3.5)
    x1.append(xnew)
    y1.append(-1.5*xnew)

x.extend(x1)
y.extend(y1)

data=[]
for i in range(len(x)):
    data.append([x[i],y[i]])


if __name__ == '__main__':

    import matplotlib.pyplot as plt

    ax = plt.subplot(111)
    ax.scatter(x,y)
    plt.show()
