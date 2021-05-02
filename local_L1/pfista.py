"""
Efficient implementation of projective FISTA.
project to space: sum(x)=1
"""


import numpy as np


def con_avg(y,a,b):
    """a is larger index while b is smaller
    
    """
    s=0
    for i in range(b,a):
        s=s+y[i]
    return (s-1)/(a-b)


def y_plus(y):
    n=y.shape[0]
    for i in range(n):
        if y[i]<0:
            y[i]=0
    return y


def proj(y):
    n=y.shape[0]
    y_des=sorted(y)
    i=n-1
    while(i!=0):
        t=con_avg(y_des,n,i)
        if t>=y_des[i-1]:
            break
        else:
            i=i-1
    t_star=con_avg(y_des,n,i)
    return(y_plus(y-t_star))




def pfista(sfunc, nsfunc, x0, max_iter=10000, max_linesearch=20, eta=2.0, tol=1e-3,
          verbose=0):

    y = x0.copy()
    x = y
    L = 1.0
    t = 1.0
    n=x0.shape[0]
    a=np.eye(n,dtype=float)
    b=np.ones((n,n))
    c=np.ones(n)

    for it in range(max_iter):
        f_old, grad = sfunc(y, True)  

        for ls in range(max_linesearch):
            y_proj = nsfunc(y - grad / L, L)
            diff = (y_proj - y).ravel()
            sqdist = np.dot(diff, diff)
            dist = np.sqrt(sqdist)

            F = sfunc(y_proj)
            Q = f_old + np.dot(diff, grad.ravel()) + 0.5 * L * sqdist

            if F <= Q:
                break

            L *= eta

        if ls == max_linesearch - 1 and verbose:
            print("Line search did not converge.")

        if verbose:
            print("%d. %f" % (it + 1, dist))

        if dist <= tol:
            if verbose:
                print("Converged.")
            break

        
        x_next = proj(y_proj) 
        t_next = (1 + np.sqrt(1 + 4 * t ** 2)) / 2.
        y = x_next + (t-1) / t_next * (x_next - x)
        t = t_next
        x = x_next

    return proj(y_proj)