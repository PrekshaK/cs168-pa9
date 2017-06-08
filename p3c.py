import numpy as np
from scipy import ndimage
from cvxpy import *
import math

m = 25
n = 5


for ind in xrange(10):
    R = np.random.normal(loc =0, scale =1, size=(m, n))
    M = R.dot(R.T)
    
    P = 0.6
    M_hat = np.zeros(shape=(m,m))
    masked = np.zeros(shape=(m,m))
    for i in xrange(m):
        for j in xrange(m):
            masked[i][j] = np.random.choice([0, 1], p=[P, 1-P])
            
    M_hat = mul_elemwise(masked, M)

    U = Semidef(m) 
    objective = Minimize(trace(U))
    constraints = [mul_elemwise(masked, U) == M_hat]
    prob = Problem(objective, constraints)
    prob.solve()
    print "the prob status is ", prob.status
    #print U.value

    diff = M - U.value
    print "diff and then norm is ", np.linalg.norm(diff, 'fro')


