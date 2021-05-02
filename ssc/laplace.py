# Author: Pengfei He <phe25@wisc.edu>
import numpy as np
import copy



def distance(x,y):

    """Calculate Euclidean distance

    Two parameter: two data points in the from of list or ndarry
    """
    if type(x)==list:
        l=len(x)
        s=0
        for i in range(l):
            s=s+(x[i]-y[i])**2
    else:
        s=(x-y)**2
    return np.sqrt(s)



def get_W(data,k):

    """Form an adjacency matrix among data points

    nearest neighbors of a point are linked to this point

    parameter
    ---------
    data: dataset
    k: number of nearest neighburs

    return
    ------
    an adjacency matrix
    """
    l=len(data)
    w=np.zeros((l,l))
    for i in range(l):
        dist=[]
        for j in range(l):
            dist.append(distance(data[i],data[j]))
        index=sorted(range(len(dist)), key=lambda k: dist[k])[1:(k+1)]
        for num in index:
            w[i][num]=1
    return w


def get_D(w):
    l=len(w)
    d=np.zeros((l,l))
    for i in range(l):
        d[i][i]=sum(w[i])
    return d


def knn_laplace(data,k):

    """calculate Laplacian of knn adjacency matrix

    parameter
    ---------
    k : number of nearest neighbors

    return
    ------
    Laplacian matrix
    """
    w=get_W(data,k)
    d=get_D(w)
    return d-w



def get_laplace(w):

    """calculate laplacian matrix given adjacency matrix

    parameter
    ---------
    adjacency matrix

    return
    ------
    laplacian matrix
    """
    d = get_D(w)
    return d-w


def extend_knn(A,B,k):
    C=copy.deepcopy(A)
    D=copy.deepcopy(B)
    m=len(A)
    n=len(B)
    for i in range(m):
        dist=[]
        for j in range(n):
            dist.append(distance(A[i],B[j]))
        index=sorted(range(len(dist)),key=lambda k: dist[k])[1:(k+1)]
        for num in index:
            if B[num] not in C:
                C.append(B[num])
                while B[num] in D:
                    D.remove(B[num])
    return C,D 


def cordinate(data,k):
    l=len(data)
    cor=[]
    for i in range(k):
        t=[]
        for j in range(l):
            t.append(data[j][i])
        cor.append(t)
    return cor



if __name__=='__main__':

    from data1 import data,x,y,z
    from kMeans import kMeans, min_k_index
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    L=knn_laplace(data, 8)
    u,v=np.linalg.eig(L)
    u=np.real(u)
    v=np.real(v)

    mdat=np.zeros((2000,3))
    mdat[:,0]=v[:,min_k_index(u,1)]
    mdat[:,1]=v[:,min_k_index(u,2)]
    mdat[:,2]=v[:,min_k_index(u,3)]

    pre_idx=kMeans(mdat,2)[:,0]

    x_1=[]
    y_1=[]
    z_1=[]
    x_2=[]
    y_2=[]
    z_2=[]
    data_1=[]
    data_2=[]
    for i in range(len(pre_idx)):
        if pre_idx[i]==0:
            x_1.append(x[i])
            y_1.append(y[i])
            z_1.append(z[i])
            data_1.append(data[i])
        else:
            x_2.append(x[i])
            y_2.append(y[i])
            z_2.append(z[i])
            data_2.append(data[i])

    ax=plt.subplot(111, projection='3d')
    ax.scatter(x_2,y_2,z_2)
    plt.show()


