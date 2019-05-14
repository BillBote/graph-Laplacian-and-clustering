from numpy import *
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from detect import distance
from detect import get_W
from detect import get_D
from detect import knn_laplace




x1=[]
y1=[]
z1=[]
for i in range(1000):
    xnew=random.uniform(-6.5,6.5)
    x1.append(xnew+random.gauss(0,0.2))
    y1.append(xnew+random.gauss(0,0.2))
    z1.append(-1.5*xnew+random.gauss(0,0.2))


data=[]
for i in range(len(x1)):
    data.append([x1[i],y1[i],z1[i]])

L=knn_laplace(data,10)
v,u=linalg.eig(L)
v=real(v)
u=real(u)

v2=copy.deepcopy(v)
v2=list(set(v2))
v2.remove(min(v2))
idx=argwhere(v==min(v2))[0][0]

ax = plt.subplot(111, projection='3d')
ax.scatter(x1,y1,z1,c=u[:,idx])
plt.show()