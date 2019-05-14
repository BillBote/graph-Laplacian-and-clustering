from numpy import *
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import simulation as sim
import copy

random.seed(1)
def generator(x,y,z):
	data=[]
	for i in range(len(x)):
		data.append([x[i],y[i],z[i]])
	return data


def distance(x,y):
    if type(x)==list:
        l=len(x)
        s=0
        for i in range(l):
            s=s+(x[i]-y[i])**2
    else:
        s=(x-y)**2
    return sqrt(s)


def get_W(data,k):
	l=len(data)
	w=zeros((l,l))
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
    d=zeros((l,l))
    for i in range(l):
        d[i][i]=sum(w[i])
    return d

def knn_laplace(data,k):
    w=get_W(data,k)
    d=get_D(w)
    return d-w

def randCent(dataSet, k):# 随机抽取k个中心
    n = len(dataSet)
    centroids = []
    x=[]
    y=[]
    for i in range(n):
        x.append(dataSet[i][0])
        y.append(data[i][1])
    for j in range(k):
        minX=min(x)
        minY=min(y)
        rangeX=float(max(x)-minX)
        rangeY=float(max(y)-minY)
        centroids.append([minX+rangeX*random.rand(1)[0],minY+rangeY*random.rand(1)[0]])
    return centroids
def kMeans(dataSet, k, distMeas = distance, createCent = randCent):
    m=len(dataSet)
    index=list(zeros(m))
    dist=list(zeros(m))
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged =False
        for i in range(m):
            minDist=inf
            minIndex=-1
            for j in range(k):
                distJ=distMeas(centroids[j],dataSet[i])
                if distJ < minDist:
                    minDist = distJ
                    minIndex = j
            if index[i]!=minIndex:
                clusterChanged = True
                index[i]=minIndex
                dist[i]=minDist**2
        for cent in range(k):
            for i in range(m):
                sx=[]
                sy=[]
                if index[i]==cent:
                    sx.append(dataSet[i][0])
                    sy.append(dataSet[i][1])
            centroids[cent]=[mean(sx),mean(sy)]
    return centroids,index,dist

data=sim.data
L=knn_laplace(data,8)
v,u=linalg.eig(L)
v=real(v)
u=real(u)

n=4

v2=copy.deepcopy(v)
v2=list(set(v2))
for i in range(n-1):
    v2.remove(min(v2))
idx=argwhere(v==min(v2))[0][0]

ax = plt.subplot(111, projection='3d')
ax.scatter(sim.x,sim.y,sim.z,c=u[:,idx])
plt.show()

"""
ax = plt.subplot(111, projection='3d')
ax.scatter(sim.x,sim.y,sim.z,c=u[1])
plt.show()

ax = plt.subplot(111, projection='3d')
ax.scatter(sim.x,sim.y,sim.z,c=u[0])
plt.show()

ax = plt.subplot(111, projection='3d')
ax.scatter(sim.x,sim.y,sim.z,c=u[2])
plt.show()

ax = plt.subplot(111, projection='3d')
ax.scatter(sim.x,sim.y,sim.z,c=u[3])
plt.show()

ax = plt.subplot(111, projection='3d')
ax.scatter(sim.x,sim.y,sim.z,c=u[4])
plt.show()

index_true=[]
for i in range(30):
	index_true.append(0)
for i in range(30,60):
	index_true.append(1)

def kMeans_1(u):
	maxu=max(u)
	minu=min(u)
	randCent=[]
	for i in range(2):
		randCent.append(minu+random.random()*(maxu-minu))
	index=zeros((800))
	dist=zeros((800))
	clusterChanged = True
	while clusterChanged:
		clusterChanged = False
		for i in range(len(u)):
			minDist=inf
			minInd=-1
			for j in range(2):
				if distance(u[i],randCent[j])<minDist:
					minDist=distance(u[i],randCent[j])
					minInd=j
			if index[i]!=minInd:
				clusterChanged = True
				index[i]=minInd
				dist[i]=minDist**2
		for cent in range(2):
			s=[]
			for j in range(len(u)):
				if index[j]==cent:
					s.append(u[j])
			randCent[cent]=mean(s)
	return index

# calculate accuracy for two objects
index_1=kMeans_1(u[1])
accuracy1=1-sum((array(index_1[400:])-array(index_true[400:]))**2)/400 # line
accuracy2=1-sum((array(index_1[:800])-array(index_true[:800]))**2)/400 #sphere
print(accuracy1)
print(accuracy2)
#print(index)

knn=get_W(data,8)
n_portion=zeros((200,4))
for i in range(len(n_portion)):
    n_portion[i][0]=knn[i][:100].sum()
    n_portion[i][1]=knn[i][100:].sum()
    n_portion[i][2]=n_portion[i][0]/8
    n_portion[i][3]=n_portion[i][1]/8
for i in range(100):
    if n_portion[i][2]<n_portion[i][3]:
        d=copy.deepcopy(knn[i])
        d[i]=2
        for j in range(100,200):
            if d[j]==1:
                d[j]=4
        ax = plt.subplot(111, projection='3d')
        ax.scatter(sim.x,sim.y,sim.z,c=d)
        plt.show()
"""

