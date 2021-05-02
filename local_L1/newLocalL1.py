#Author: Pengfei He <phe25@wisc.edu>

import numpy as np 
from laplace import distance
from sklearn.linear_model import Lasso
from localPista import LocalRegressor
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



def locaL(data,indexs,B,alpha,beta):
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
        oscar_owl = LocalRegressor(alpha,beta)
        oscar_owl.fit(X,Y)
        B=store(oscar_owl.coef_,B,index)
    return B