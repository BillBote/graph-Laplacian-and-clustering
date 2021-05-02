import numpy as np
from data1 import data,x,y,z
import matplotlib.pyplot as plt
from sklearn.linear_model import Lasso
from pyowl import OwlRegressor
from mpl_toolkits.mplot3d import Axes3D
from laplace import get_laplace, knn_laplace,extend_knn,cordinate
from kMeans import kMeans, min_k_index, max_k_index
import copy

def store(coef,B,index):
    n=len(coef)
    if index == 0:
        for i in range(n):
            B[i+1,index]=coef[i]
    elif index==n:
        for i in range(n):
            B[i,index]=coef[i]
    else:
        for i in range(index):
            B[i,index]=coef[i]
        for i in range(index,n):
            B[i+1,index]=coef[i]
    return B


def reshapeL(l):
    n=len(l)
    m=len(l[0])
    L=[]
    for i in range(m):
        x=[]
        for j in range(n):
            x.append(X[j][i])
        L.append(x)
    return L


def get_B(data,indexs,B,alpha,beta):
    n_sample=len(data[0])
    n_feature=len(data)
    for index in indexs:
        X=np.zeros((n_sample,n_feature-1))
        if index == 0:
            for i in range(n_feature-1):
                X[:,i]=data[i+1]
        elif index == n_feature-1:
            for i in range(n_feature-1):
                X[:,i]=data[i]
        else:
            for i in range(index):
                X[:,i]=data[i]
            for i in range(index,n_feature-1):
                X[:,i]=data[i+1]
        Y=np.array(data[index])
        #oscar_owl = OwlRegressor(weights=np.ones(n_feature-1) * alpha)
        #oscar_owl.fit(X,Y)
        #B=store(oscar_owl.coef_,B,index)
        oscar_owl = OwlRegressor(weights=(alpha,beta))
        oscar_owl.fit(X,Y)
        B=store(oscar_owl.coef_,B,index)
        #lasso=Lasso(alpha,max_iter=10000)
        #lasso.fit(X,Y)
        #B=store(lasso.coef_,B,index)
    return B


n_sample=len(data[0])
n_feature=len(data)

alpha=0.0001
beta=0.01
k=200

indexs=np.random.choice(range(n_feature),k)
B=np.zeros((n_feature,n_feature))

B=get_B(data,indexs,B,alpha,beta)
B=np.abs(B)
W=B+B.T

nonzero=[]
for index in range(1000):
    nonzero.append(np.count_nonzero(B[:,index]))
s=[]
for i in range(1000):
    if nonzero[i]!=0:
        s.append(i)
print(s)

index=s[0]

n=10
idx=[]
for i in range(2,n+1):
    idx.append(min_k_index(B[:,index],i))
s=0
for i in idx:
    if i>1000:
        s=s+1
print(s)

ax=plt.subplot(111,projection='3d')
ax.scatter(x,y,z,color='yellow')
ax.scatter(x[index],y[index],z[index],color='red')
ax.scatter(x[idx[0]],y[idx[0]],z[idx[0]],color='midnightblue')
ax.scatter(x[idx[1]],y[idx[1]],z[idx[1]],color='blue')
ax.scatter(x[idx[2]],y[idx[2]],z[idx[2]],color='mediumslateblue')
ax.scatter(x[idx[3]],y[idx[3]],z[idx[3]],color='dodgerblue')
ax.scatter(x[idx[4]],y[idx[4]],z[idx[4]],color='deepskyblue')
ax.scatter(x[idx[5]],y[idx[5]],z[idx[5]],color='lightskyblue')
ax.scatter(x[idx[6]],y[idx[6]],z[idx[6]],color='powderblue')
plt.show()