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
br = np.dot(A[0:r], x)


xbar = cvx.Variable(1200)
Ar = A[0:r]
dotpr = np.dot(A[0:r], xbar)

constraints = [xbar >= 0]
for i in xrange(r):
    # tosum = [Ar[i][j]*xbar[i] for j in xrange(1200)]
    summation = 0
    for j in xrange(1200):
        summation += Ar[i][j]*xbar[i]

    #print tosum
    #summation = cvx.sum_entries(tosum)
    #print summation
    bri = br[i] + 10**-5
    brii = br[i] - 10**-5
    #constraints.append(summation >= brii)
    constraints.append(summation <= bri)


obj = cvx.Minimize(cvx.norm(xbar, 1))
prob = cvx.Problem(obj, constraints)
prob.solve()

print "status is ", prob.status
print xbar.value
