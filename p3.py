import numpy as np
from scipy import ndimage
from cvxpy import *
import math

m = 25
n = 5
R = np.random.normal(loc =0, scale =1, size=(m, n))
M = R.dot(R.T)

P = 0.6
M_hat = M
for i in xrange(m):
    for j in xrange(n):
        M_hat[i][j] = np.random.choice([0, M[i][j]], p=[P, 1-P])

# Now recover M from M_hat using cvx
# U = variable
# Minimize rank(U)
# Constraint that U matches the known entries of M_hat.

# AU = eigenvalues of U
# Minimize L1 norm of AU
# Constraints are:
# U is symmetric 
# U matches the known entries of M_hat
# AU is non-negative

# Minimize sum of diagonal entries of U
# Constraints are:
# U is symmetric
# U is positive semidefinite
# U matches the known entries of M_hat


U = Variable(m, m)                     # Semi definite positive matrix of dim m,m
objective = Minimize(lambda_sum_largest(U, m))

# Constraint that U matches the known entries of M_hat is confusing
# Need to do masking first
constraints = [U == M_hat, U >> 0]

prob = Problem(objective, constraints)
prob.solve()
print U.value 

# returns None for now



