from PIL import Image
from numpy import array
import matplotlib.pyplot as plt

img = array(Image.open("corrupted.png"), dtype=int)[:,:,0]
Known = (img > 0).astype(int)

naive_img = array(img)

for i in xrange(203):
  for j in xrange(143):
    if naive_img[i][j] == 0:
      summ = 0
      num_neigh = 0

      # update spots with avg(known neighbors)
      if (i==0 and j==0):
        summ = (naive_img[i][j+1] + naive_img[i+1][j])
        if naive_img[i][j+1] > 0:
          num_neigh+=1
        if naive_img[i+1][j] > 0:
          num_neigh+=1
      elif (i==0 and j==142):
        summ = (naive_img[i][j-1] + naive_img[i+1][j])
        if naive_img[i][j-1] > 0:
          num_neigh+=1
        if naive_img[i+1][j] > 0:
          num_neigh+=1
      elif (i==202 and j==0):
        summ = (naive_img[i][j+1] + naive_img[i-1][j])
        if naive_img[i][j+1] > 0:
          num_neigh+=1
        if naive_img[i-1][j] > 0:
          num_neigh+=1
      elif (i==202 and j==142):
        summ = (naive_img[i][j-1] + naive_img[i-1][j])
        if naive_img[i][j-1] > 0:
          num_neigh+=1
        if naive_img[i-1][j] > 0:
          num_neigh+=1

      elif (i>0 and i<202 and j>0 and j<142):
        summ = (naive_img[i][j-1] + naive_img[i][j+1] + naive_img[i-1][j] + naive_img[i+1][j])
        if naive_img[i][j-1] > 0:
          num_neigh+=1
        if naive_img[i][j+1] > 0:
          num_neigh+=1
        if naive_img[i-1][j] > 0:
          num_neigh+=1
        if naive_img[i+1][j] > 0:
          num_neigh+=1

      else:
        if (i==0 and j<142 and j>0):
          summ = (naive_img[i][j-1] + naive_img[i][j+1] + naive_img[i+1][j])
          if naive_img[i][j-1] > 0:
            num_neigh+=1
          if naive_img[i][j+1] > 0:
            num_neigh+=1
          if naive_img[i+1][j] > 0:
            num_neigh+=1
          
        if (j==0 and i<202 and i>0):
          summ = (naive_img[i][j+1] + naive_img[i-1][j] + naive_img[i+1][j])
          if naive_img[i][j+1] > 0:
            num_neigh+=1
          if naive_img[i-1][j] > 0:
            num_neigh+=1
          if naive_img[i+1][j] > 0:
            num_neigh+=1
          
        if (i==202 and j<142 and j>0):
          summ = (naive_img[i][j-1] + naive_img[i][j+1] + naive_img[i-1][j])
          if naive_img[i][j-1] > 0:
            num_neigh+=1
          if naive_img[i][j+1] > 0:
            num_neigh+=1
          if naive_img[i-1][j] > 0:
            num_neigh+=1
          
        if (j==142 and i<202 and i>0):
          summ = (naive_img[i][j-1] + naive_img[i-1][j] + naive_img[i+1][j])
          if naive_img[i][j-1] > 0:
            num_neigh+=1
          if naive_img[i-1][j] > 0:
            num_neigh+=1
          if naive_img[i+1][j] > 0:
            num_neigh+=1

      if num_neigh > 0:
        naive_img[i][j] = ((summ*1.0)/num_neigh)

plt.imshow(naive_img)
plt.gray()
plt.savefig('recovered_stanford_tree_2b.png')  
plt.show()

from cvxpy import Variable, Minimize, Problem, mul_elemwise, tv
U = Variable(*img.shape)
obj = Minimize(tv(U))
constraints = [mul_elemwise(Known, U) == mul_elemwise(Known, img)]
prob = Problem(obj, constraints)
prob.solve()
# recovered image is now in U.value
plt.imshow(U.value)
plt.gray()
plt.savefig('recovered_stanford_tree_2c.png')
plt.show()