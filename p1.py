
#-----------------------------------1 B------------------------------------

import numpy as np
from scipy import ndimage
from cvxpy import *
import math
import matplotlib.pyplot as plt

mean, var = 0, 1
m = 1200
A = np.random.normal(loc =0, scale =1, size=(m, m))

text_file = open("p9_images/wonderland-tree.txt", "r")
# 0 is black, 1 is white
lines = text_file.readlines()
x = []
for line in lines:
    for i in line.strip('\n'):
        x.append(int(i))

r = 600
Ar = A[0:r]
br = np.dot(Ar, x)


xbar = Variable(m)
objective = Minimize(norm(xbar, 1))
constraints = [0 <= xbar, xbar <= 1, Ar*xbar - br == 0]
prob = Problem(objective, constraints)
prob.solve()
print xbar.value 

print "norm of xbar is ", np.linalg.norm(xbar.value, ord=1)
print "norm of x is ", np.linalg.norm(x, ord=1)



#--------------------------------1 C---------------------------------------------



def findOptimal(r):
    Ar = A[0:r]
    br = np.dot(Ar, x)

    xbar = Variable(m)
    objective = Minimize(norm(xbar, 1))
    constraints = [0 <= xbar, xbar <= 1, Ar*xbar - br == 0]
    prob = Problem(objective, constraints)
    prob.solve()

    norm_xbar = np.linalg.norm(xbar.value, ord=1)
    norm_x = np.linalg.norm(x, ord=1)   

    diff = [math.fabs(x[i] - xbar.value[i]) for i in xrange(len(x))]
    norm_diff = np.linalg.norm(diff, ord=1)
    print "norm diff ", norm_diff
    return norm_diff

def binarySearch(rs, start, end, R):
    r = R
    if start > end:
        print "so the least r is ", r
        return r

    mid = (start + end)/2
    candidate = rs[mid]
    print "candidate ", candidate

    if findOptimal(candidate) <= 0.001:
        r = candidate
        return binarySearch(rs, start, mid-1, r)

    elif findOptimal(candidate) > 0.001:
        return binarySearch(rs, mid+1, end, r)

rs = [i for i in xrange(600)]
least_r = binarySearch(rs, 0, len(rs)-1, -1)
print "least r is ", least_r


#------------------------------------1 D----------------------------------------------

r_sts = [i for i in xrange(least_r-11, least_r+3)]

norm_diffs = []

for r in r_sts:
    norm_diff = findOptimal(r)
    norm_diffs.append(norm_diff)
plt.plot(r_sts, norm_diffs)
plt.show()


