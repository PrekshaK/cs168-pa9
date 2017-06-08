import numpy as np
from scipy import ndimage
from cvxpy import *
import math

m = 5
n = 3
R = np.random.normal(loc =0, scale =1, size=(m, n))
M = R.dot(R.T)

P = 0.6
M_hat = M
for i in xrange(m):
    for j in xrange(n):
        M_hat[i][j] = np.random.choice([0, M[i][j]], p=[P, 1-P])


# According to question

# Now recover M from M_hat using cvx
# U = variable

# Minimize rank(U)
# Constraint that U matches the known entries of M_hat.

#           can be restates as:
# AU = eigenvalues of U
# Minimize L1 norm of AU
# Constraints are:
# U is symmetric 
# U matches the known entries of M_hat
# AU is non-negative

#           can be restated as
# Minimize sum of diagonal entries of U
# Constraints are:
# U is symmetric
# U is positive semidefinite
# U matches the known entries of M_hat


masked = np.ma.masked_where(M_hat==0, M_hat)
print "norm of M_hat is ", np.linalg.norm(M_hat, ord=1)

U = Variable(m, m) 
objective = Minimize(trace(U))

# Constraint that U matches the known entries of M_hat is confusing    
constraints = []
constraints.append(U>>0)
for i in xrange(m):
    for j in xrange(len(masked.mask[i])):
        if masked.mask[i][j] == False:
            constraints.append(U[i, j] == masked[i][j])

prob = Problem(objective, constraints)
print "the prob status is ", prob.status
prob.solve()
print np.linalg.norm(U.value, ord=1)

