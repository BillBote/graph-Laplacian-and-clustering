import numpy as np
from data9 import data,x,y,z
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso
from pyowl import OwlRegressor
from mpl_toolkits.mplot3d import Axes3D
from laplace import get_laplace, knn_laplace,extend_knn,cordinate, distance
from kMeans import kMeans, min_k_index, max_k_index
from LocalL1 import locaL1
import copy

n_sample=len(data[0])
n_feature=len(data)

alpha=0.0000001
K=700
k1=200
k2=900

indexs=np.random.choice(range(n_feature),K)
B=np.zeros((n_feature,n_feature))

B=locaL1(data,indexs,B,alpha,k1,k2)
B=np.abs(B)

L=get_laplace(B)
u,v=np.linalg.eig(L)
v=np.real(v)
u=np.real(u)

ax = plt.subplot(111, projection='3d')
ax.scatter(x,y,z,c=v[:,min_k_index(u,2)])

plt.show()

mdat1=np.zeros((n_feature,1))
mdat1[:,0]=v[:,min_k_index(u,2)]

pre_idx1=kMeans(mdat1,2)[:,0]

x_1=[]
y_1=[]
z_1=[]
x_2=[]
y_2=[]
z_2=[]
data_1=[]
data_2=[]
for i in range(len(pre_idx1)):
    if pre_idx1[i]==0:
        x_1.append(x[i])
        y_1.append(y[i])
        z_1.append(z[i])
        data_1.append(data[i])
    else:
        x_2.append(x[i])
        y_2.append(y[i])
        z_2.append(z[i])
        data_2.append(data[i])

ax = plt.subplot(111, projection='3d')
ax.scatter(x_2,y_2,z_2)
plt.show()
ax = plt.subplot(111, projection='3d')
ax.scatter(x_1,y_1,z_1)
plt.show()