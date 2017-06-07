import numpy as np
from scipy import ndimage
from PIL import Image
import cvxpy as cvx

mean, var = 0, 1
A = np.random.normal(loc =0, scale =1, size=(1200, 1200))

text_file = open("p9_images/wonderland-tree.txt", "r")
lines = text_file.readlines()
x = []
for line in lines:
    for i in line.strip('\n'):
        x.append(int(i))

#print x[0:100]
r = 100
Ar = A[0:r]
br = np.dot(Ar, x)


xbar = cvx.Variable(1200)
constraints = []

for i in xrange(r):
    summation = 0
    summation = A[i]*xbar
    bri = br[i] + 10**-5
    brii = br[i] - 10**-5
    constraints.append(summation >= brii)
    constraints.append(summation >= bri)
    constraints.append(xbar[i] > 0)

obj = cvx.Minimize(cvx.norm(xbar, 1))
prob = cvx.Problem(obj, constraints)

prob.solve()

print "norm of original x is ", np.linalg.norm(x, ord=1)

print "status is ", prob.status

print np.linalg.norm(xbar.value, ord=1)









