"""
Author: Pengfei He
Date: 05/04/2019
Aim: Contains functions for detecting  objects
Details: graph Laplacian function; kMeans clustering function
"""


import numpy as np
import random
import copy


def distance(x,y):
    if type(x)==list:
        l=len(x)
        s=0
        for i in range(l):
            s=s+(x[i]-y[i])**2
    else:
        s=(x-y)**2
    return np.sqrt(s)


def get_W(data,k):
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

# unnormalized laplace 
def knn_laplace(data,k):
    w=get_W(data,k)
    d=get_D(w)
    return d-w

# normalized laplace
def knn_laplace_n(data,k):
    w=get_W(data,k)
    d=get_D(w)
    return np.identity(len(w))-np.matmul(np.linalg.inv(d),w)

def distEclud(vecA, vecB):
    return np.sqrt(np.sum(np.power(vecA - vecB, 2)))

def randCent(dataSet, k):
    n = np.shape(dataSet)[1]
    centroids = np.mat(np.zeros((k,n)))
    for j in range(n):
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = minJ + rangeJ * np.random.rand(k,1)
    return centroids

def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):
    m = np.shape(dataSet)[0]
    clusterAssment = np.mat(np.zeros((m,2)))
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = np.inf; minIndex = -1
            for j in range(k):
                distJI = distMeas(centroids[j,:],dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
        for cent in range(k):
            ptsInClust = dataSet[np.nonzero(clusterAssment[:,0].A==cent)[0]]
            centroids[cent,:] = np.mean(ptsInClust, axis=0)
    return clusterAssment

def min_k_index(v,k):  #get kth smallest eigenvalue
    v2=copy.deepcopy(v)
    v2=list(set(v2))
    for i in range(k-1):
        v2.remove(min(v2))
    idx=np.argwhere(v==min(v2))[0][0]
    return idx


def accuracy(true_idx,pre_idx):
    n=true_idx.shape[0]
    t=np.count_nonzero(true_idx-pre_idx==0)
    return t/n







