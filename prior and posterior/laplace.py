import numpy as np
import random
import pre
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

x_sim=pre.x_sim
y_sim=pre.y_sim
n=pre.n

def distance(x,y):  #calculate distance between x and y
    d=(x[0]-y[0])**2+(x[1]-y[1])**2+(x[2]-y[2])**2
    return d
    
def k(x,y,epsilon,n=500,m=3): # calculate Kernel function K_epsilon
    alpha=4/3*np.pi
    if distance(x,y)<=epsilon:
        return (m+2)/(n**2*alpha*epsilon**(m+2))
    else:
        return 0

def Un(alpha,s,k): # calculate Karhunen-Loeve expansion u_n
    p=np.random.normal(0,1,k)
    un=np.zeros((1,500))
    for i in range(k):
        un=un+(alpha+a[i])**(-s/4)*p[i]*v[i]
    return un

def w(i,sigma):  # Observation Maps w
    s=0
    for j in range(400):
        if distance(x_sim[i],x_sim[j])<=sigma**2:
            s=s+pre.u(x_sim[j])
    return 1/(n*4/3*np.pi)*s

def phi(x,y,sigma): #noise model phi
    l=len(x)
    s=0
    for i in range(l):
        s=s+(x[i]-y[i])**2
    return 1/(2*sigma**2)*s

W=np.zeros((500,500)) # calculate matrix W
for i in range(500):
    for j in range(500):
        W[i,j]=k(x_sim[i],x_sim[j],n**(-1/4))

D=np.zeros((500,500)) #calculate matrix D
for i in range(500):
    D[i,i]=np.sum(W[i])

Laplace=D-W #calculate Graph Laplacian operator matrix
a,v=np.linalg.eig(Laplace) # get eigenvalue and eigenvector for Laplacian matrix
a=np.real(a)
v=np.real(v)
prior=Un(0,4,400)[0] # calculate prior distribution
ma=max(prior)  #normalization
mi=min(prior)
prior=2*(prior-mi)/(ma-mi)-1



w_new=[] #calculate observation for x
for i in range(400):
    w_new.append(w(i,0.1))

post=phi(y_sim,w_new,0.1)*Un(0,4,400)[0] # calculate posterior distribution
Ma=max(post)  #normalization
Mi=min(post)
post=2*(post-Mi)/(Ma-Mi)-1


#plot
col=[]
for i in range(400):
    col.append(x_sim[i][0])
ind=[]
for i in range(400):
    ind.append(x_sim[i][1])
dim=[]
for i in range(400):
    dim.append(x_sim[i][2])

ax = plt.subplot(111, projection='3d')
ax.scatter(col,ind,dim,c=prior[:400])
plt.show()

ax = plt.subplot(111, projection='3d')
ax.scatter(col,ind,dim,c=post[:400])
plt.show()
