# Matrix Algebra
import numpy as np

A = np.matrix('1 2 3; 2 7 4')
B = np.matrix('1 -1; 0 1')
C = np.matrix('5 -1; 9 1; 6 0')
D = np.matrix('3 -2 -1; 1 2 3')
u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.matrix('1;8;0;5')

A.shape
B.shape
C.shape
D.shape
u.shape
v.shape
w.shape

#1. Matrix Dimensions
#1.1) Dimensions of A: 2x3  
#1.2) Dimensions of B: 2x2
#1.3) Dimensions of C: 3x2
#1.4) Dimensions of D: 2x3
#1.5) Dimensions of u: 1x4
#1.6) Dimensions of w: 4x1

#2. Vector Operations
#2.1) u + v = array([ 9,  7, -4,  9])
#2.2) u - v = array([ 3, -3, -2,  1])
#2.3) 6*u = array([ 36,  12, -18,  30])
#2.4) u dot product v = 51
np.dot(u,v)

#2.5) norm (length) of u = 8.6023252670426267
np.linalg.norm(u)

#3. Matrix Operations
#3.1) A + C = not defined
#3.2) A - C(transpose) = matrix([[-4, -7, -3],
#                               [ 3,  6,  4]])
A - np.matrix.transpose(C)
#3.3) C(transpose) + 3D = matrix([[14,  3,  3],
#                                 [ 2,  7,  9]])
np.matrix.transpose(C) + (3*D)

#3.4) B*A = matrix([[-1, -5, -1],
#                   [ 2,  7,  4]])

#3.5) B*A(transpose) = not defined
B*np.matrix.transpose(A)

#3.6) B*C = not defined
#3.7) C*B = matrix([[ 5, -6],
#                   [ 9, -8],
#                   [ 6, -6]])

#3.8) B**4 = matrix([[ 1, -4],
#                    [ 0,  1]])
        
#3.9) A * A(transpose) = matrix([[14, 28],
#                                [28, 69]])
A* np.matrix.transpose(A)

#3.10) D(transpose)*D = matrix([[10, -4,  0],
#                               [-4,  8,  8],
#                               [ 0,  8, 10]])
np.matrix.transpose(D)*D
