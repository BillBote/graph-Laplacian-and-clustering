# Author: Pengfei He <phe25@wisc.edu>

import numpy as np
import copy


def randCent(dataSet, k):

    """randomly choose k centers
    """

    n = np.shape(dataSet)[1]
    centroids = np.mat(np.zeros((k,n)))
    for j in range(n):
        minJ = min(dataSet[:,j])
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:,j] = minJ + rangeJ * np.random.rand(k,1)
    return centroids



def distEclud(vecA, vecB):

    """calculate Euclidean distance
    """

    return np.sqrt(np.sum(np.power(vecA - vecB, 2)))



def kMeans(dataSet, k, distMeas=distEclud, createCent=randCent):

    """kMeans clustering

    parameter
    ---------
    k : number of clusterings
    distMeas : type of distance
    createCent : initial centers

    return
    ------
    set of indexes
    """
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



def min_k_index(v,k):

    """return kth smallest element of a set
    """

    v2=copy.deepcopy(v)
    v2=np.abs(v2)
    v2=list(set(v2))
    for i in range(k-1):
        v2.remove(min(v2))
    idx=np.argwhere(np.abs(v)==min(v2))[0][0]
    return idx

def max_k_index(v,k):
    
    """return kth bigest element of a set
    """

    v2=copy.deepcopy(v)
    v2=np.abs(v2)
    v2=list(set(v2))
    for i in range(k-1):
        v2.remove(max(v2))
    idx=np.argwhere(np.abs(v)==max(v2))[0][0]
    return idx
