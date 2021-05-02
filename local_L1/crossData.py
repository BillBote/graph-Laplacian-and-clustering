import numpy as np 

x=[]
y=[]
z=[]

# line 1
x1=[]
y1=[]
z1=[]

t=np.arange(-4,4,0.016)
for i in range(len(t)):
	x1.append(0)
	y1.append(0)
	z1.append(t[i])

x.extend(x1)
y.extend(y1)
z.extend(z1)

#line 2
x2=[]
y2=[]
z2=[]

for i in range(len(t)):
	x2.append(0)
	y2.append(t[i])
	z2.append(0)

x.extend(x2)
y.extend(y2)
z.extend(z2)

data=[]
for i in range(len(x)):
    data.append([x[i],y[i],z[i]])



if __name__ == '__main__':

    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D

    ax = plt.subplot(111, projection='3d')
    ax.scatter(x,y,z)
    plt.show()

