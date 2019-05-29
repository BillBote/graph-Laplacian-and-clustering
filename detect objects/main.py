"""
Author: Pengfei He
Date: 05/10/2019
Aim: main file for experiment
"""

import numpy as np
import detect
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sphere_line
#import lines_lines
#import lines_plane


data1=sphere_line.data
x=sphere_line.x
y=sphere_line.y
z=sphere_line.z
n1=len(data1)

L1=detect.knn_laplace(data1,8)
u1,v1=np.linalg.eig(L1)
u1=np.real(u1)
v1=np.real(v1)

idx1=detect.min_k_index(u1,2)
idx2=detect.min_k_index(u1,3)
ax=plt.subplot(111, projection='3d')
ax.scatter(x,y,z,c=v1[:,detect.min_k_index(u1,2)])
plt.show()
mdat1=np.zeros((n1,2))
mdat1[:,0]=v1[:,idx1]
mdat1[:,1]=v1[:,idx2]
pre_idx1=detect.kMeans(mdat1,2)[:,0]

x_1=[]
y_1=[]
z_1=[]
x_2=[]
y_2=[]
z_2=[]
for i in range(len(pre_idx1)):
    if pre_idx1[i]==0:
        x_1.append(x[i])
        y_1.append(y[i])
        z_1.append(z[i])
    else:
        x_2.append(x[i])
        y_2.append(y[i])
        z_2.append(z[i])

ax=plt.subplot(111, projection='3d')
ax.scatter(x_2,y_2,z_2)
plt.show()
