#Author: Pengfei He <phe25@wisc.edu>

import numpy as np 
from laplace import distance
from consowl import OwlRegressor
import copy

def local_store(B,coef,index):

    """store coefficients into similarity matrix for local

    parameters
    ----------
    B: a materix to store coefficients in
    coef: a dictionary whose key is index and value is corresponding coefficient
    index: index of a point which is the respondent variable for regression
    """
    for item in coef:
        B[item,index]=coef[item]
    return B


def k_neighbor(point,data,k):

    """obtain K nearest neighbors for a given point

    parameter
    ---------
    point: the point whose neghbors are found
    data: dataset
    k: number of neighbors
    """
    n=len(data)
    dist=[]
    for i in range(n):
        dist.append(distance(point,data[i]))
    index=sorted(range(len(dist)), key=lambda k: dist[k])[1:(k+1)]
    return index


def neighborhood(point,data,epsilon):

    """obtain neighbors inside a neighborhood with given radius

    parameter
    ---------
    point: the point whose neighbors are found
    data: dataset
    epsilon: radius of the neighborhood
    """

    n=len(data)
    index=[]
    for i in range(n):
        if distance(point,data[i])<epsilon and distance(point,data[i])!=0:
            index.append(i)
    return index


def localL1(data,indexs,B,alpha,k1,k2):

    """do local l1 regression and store coefficients in a matrix

    parameter
    ---------
    data: dataset
    indexs: set of index
    B: store matrix
    alpha: parameter of l1 regression
    k1: number of neighbors for regression
    k2: number of actual neighbors we picked to connect
    """
    n_sample=len(data[0])
    for index in indexs:
        kIndex=k_neighbor(data[index],data,k1)
        X=np.zeros((n_sample,k1))
        for i in range(k1):
            X[:,i]=data[kIndex[i]]
        Y=np.array(data[index])
        owl=OwlRegressor(weights=alpha*np.ones(k1))
        owl.fit(X,Y)
        coef=owl.coef_
        dic={}
        for i in range(len(coef)):
            dic[coef[i]]=i
        if np.count_nonzero(coef)<=k2:
            for i in range(k1):
                B[kIndex[i],index]=coef[i]
        else:
            coef1=sorted(coef,reverse=True)
            for i in range(k2):
                B[kIndex[dic[coef1[i]]],index]=coef1[i]
    return B



def localL1_2(data,indexs,B,alpha,epsilon):

    """do local l1 regression and store coefficients in a matrix

    parameter
    ---------
    data: dataset
    indexs: set of index
    B: store matrix
    alpha: parameter of l1 regression
    epsilon: radius
    """
    
    n_sample=len(data[0])
    for index in indexs:
        kIndex=neighborhood(data[index],data,epsilon)
        n1=len(kIndex)
        X=np.zeros((n_sample,n1))
        for i in range(n1):
            X[:,i]=data[kIndex[i]]
        Y=np.array(data[index])
        owl=OwlRegressor(weights=alpha*np.ones(n1))
        owl.fit(X,Y)
        coef=owl.coef_
        for i in range(n1):
             B[kIndex[i],index]=coef[i]
    return B



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



def pOWL(data,indexs,B,w):
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
        owl = OwlRegressor(w)
        owl.fit(X,Y)
        B=store(owl.coef_,B,index)
    return B