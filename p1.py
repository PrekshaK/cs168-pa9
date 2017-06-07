import numpy as np
from scipy import ndimage
from PIL import Image
from cvxpy import *

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
print "Optimal value", prob.solve()
print "Optimal var"
print xbar.value 

print "norm of xbar is ", np.linalg.norm(xbar.value, ord=1)
print "norm of x is ", np.linalg.norm(x, ord=1)

