"""
Date:04/07/2019
Author:Pengfei He
Aim: simulation of x and y
"""

import numpy as np
import random


np.random.seed(0)
n=500
p=400

def u(x_list): #choose function u
	return(x_list[0]+x_list[1]+x_list[2])

x_sim=[]  #simulation of x
for i in range(n):
	x=np.random.normal(0,1,3)
	x_sim.append(list(x))

y_sim=[] #simulation of y
for i in range(p):
	y=u(x_sim[i])
	y_sim.append(y)


