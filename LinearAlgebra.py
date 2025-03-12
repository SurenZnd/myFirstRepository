import numpy as np
from numpy.linalg import eig,inv,matmul, svd

A = np.array([[1, 3],[3,1]])
print("Matrix A:",A)

w,v = eig(A)
print("Eigenvalues of A:",w)
print("Eigenvectors of A:",v)

