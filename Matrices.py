from __future__ import division
from MatrixToolkit import *
import copy

def LUDecomposition(A):
	n = len(A)
	
	#java equiv. to array = new int[n][n]...python is not always simpler
	U = [ [ 0 for i in range(n) ] for j in range(n) ] 
	L = [ [ 0 for i in range(n) ] for j in range(n) ]
	
	#initialize U with 0s below the diagonal--nm...that's already done
	#initialize L with 1s on the diagonal and 0s above the diagonal
	for jc in range(n):
		L[jc][jc] = 1
	
	
	for k in range(n):
		U[k][k] = A[k][k]
		for i in range(k+1, n):
			L[i][k] = A[i][k]/U[k][k] # L[i][k] holds v_i
			U[k][i] = A[k][i]         # U[k][i] holds w_i^T
		for i in range(k+1, n):
			for j in range(k+1, n):
				A[i][j] = A[i][j] - L[i][k] * U[k][j]
	
	return L, U
	
def LUPDecomposition(A):
	n = len(A)
	
	pi = [ i for i in range(n) ]
	
	printM(A)
	print pi
	raw_input()
	
	for k in range(n):
		k1 = 0
		p = 0
		for i in range(k, n):
			if abs( A[i][k] ) > p:
				p = abs( A[i][k] )
				k1 = i
		if p == 0:
			print "error: singular matrix!"
		pi[k], pi[k1] = pi[k1], pi[k]
		printM(A)
		print pi
		raw_input()
		
		for i in range(n):
			A[k][i], A[k1][i] = A[k1][i], A[k][i]
			print "Yo"
			printM(A)
			print pi
			raw_input()
		
		for i in range(k+1, n):
			A[i][k] = A[i][k]/A[k][k]
			printM(A)
			print pi
			raw_input()
			for j in range(k+1, n):
				A[i][j] = A[i][j] - A[i][k] * A[k][j]
				printM(A)
				print pi
				raw_input()
	
	return A, pi
				


#Special version that prints				
def LUDecompositionP(A):
	n = len(A)
	
	printM(A)
	
	#java equiv. to array = new int[n][n]...python is not always simplier
	U = [ [ 0 for i in range(n) ] for j in range(n) ] 
	L = [ [ 0 for i in range(n) ] for j in range(n) ]
	
	printM(U)
	
	#time.sleep(1)
	#raw_input()
	
	#initialize U with 0s below the diagonal--nm...that's already done
	#initialize L with 1s on the diagonal and 0s above the diagonal
	for jc in range(n):
		L[jc][jc] = 1
	
	printA( (L, "L"), (U, "U"), (A, "A"))
	raw_input()
	
	for k in range(n):
		U[k][k] = A[k][k]
		for i in range(k+1, n):
			L[i][k] = A[i][k]/U[k][k] # L[i][k] holds v_i
			printA( (L, "L"), (U, "U"), (A, "A"))
			raw_input()
			U[k][i] = A[k][i]         # U[k][i] holds w_i^T
			printA( (L, "L"), (U, "U"), (A, "A"))
			raw_input()
		for i in range(k+1, n):
			for j in range(k+1, n):
				A[i][j] = A[i][j] - L[i][k] * U[k][j]
				printA( (L, "L"), (U, "U"), (A, "A"))
				raw_input()
	
	return L, U
	
def LUPSolve(L, U, pi, b):
	n = len(L)
	x = [0.0 for jc in range(n)]
	y = [0.0 for jc in range(n)]
	for i in range(n):
		summation = 0.0
		for j in range(i): #same as summation on line 4
			summation += L[i][j]*y[j]
		y[i] = b[pi[i]] - summation
	for i in reversed(range(n)):
		summation = 0.0
		for j in range(i+1, n): #stand in for the summation on line 6
			summation += U[i][j]*x[j]
		x[i] = (y[i] - summation)/U[i][i]
	return x
	
#testMatrix = [[1, 2, 0], [3, 4, 4,], [5, 6, 3]]
testMatrix = [[2,3,1,5], [6,13,5,19], [2,19,10,23], [4,10,11,31]]
equalsMatrix = [8, 5, 3, 7]

testMatrix2 = [[1, 5, 4], [2, 0, 3], [5, 8, 2]]
equalsMatrix2 = [[12], [9], [5]]
equalsMatrix21 = [12, 9, 5]

testMatrix3 = [[2,0,2,.6],[3,3,4,-2],[5,5,4,2],[-1,-2,3.4,-1]]

#LUPDecomposition(testMatrix)
""" THIS IS FOR THE DEMONSTATION OF LU FACTORIZATION """"""
L, U = LUDecompositionP(testMatrix2)
print "L"
printM(L)
print "U"
printM(U)
print "L x U"
printM(mult(L, U))
"""

#can change to testmatrix2 or test matrix 3
A1 = copy.deepcopy(testMatrix2)
A1, pi = LUPDecomposition(A1)

print "A1"
printM(A1)
print "pi: " + str(pi)


L, U = splitLU(A1)

"""Show that PA = LU """
P = explodePI(pi)
print "L"
printM(L)
print "U"
printM(U)
print "P"
printM(P)
print "A"
printM(testMatrix2)
print "L x U"
printM(mult(L, U))
print "P x A"
printM(mult(P, testMatrix2))
""""""

sol = LUPSolve(L, U, pi, equalsMatrix21)

print "Solution"
printM(sol)

print "Actual solution matrix:"
act = [-3/19,-1/19,59/19]
printM(act)

