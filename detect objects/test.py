import numpy as np
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import copy
from data7 import x,y,z,data
from detect import distance,get_W, get_D,knn_laplace, min_k_index

# plot data1
ax = plt.subplot(111, projection='3d')
ax.scatter(x,y,z)

L=knn_laplace(data,8)
u,v=np.linalg.eig(L)
u=np.real(u)
v=np.real(v)


ax = plt.subplot(111, projection='3d')
ax.scatter(x,y,z,c=v[:,min_k_index(u, 2)])
plt.show()