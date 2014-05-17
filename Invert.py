from __future__ import division
from MatrixToolkit import *

def invert(A):
	n = len(A)
	
	#java equiv. to array = new int[n][n]...python is not always simpler
	I = [ [ 0 for i in range(n) ] for j in range(n) ] 
	
	#initialize I with 1s on the diagonal and 0s above the diagonal
	for jc in range(n):
		I[jc][jc] = 1
		
	for jc in range(n):
		A[jc] += I[jc]
		
	m = len(A[0])
	
	printM(A)
	raw_input()
	
	#Row Reduction time!
	for k in range(n):
		lilyBriggs = A[k][k]
		for i in range(k, m):
			A[k][i] = A[k][i]/lilyBriggs
			printM(A)
			raw_input()
		for i in range(k+1, n):
			johnCharles = A[i][k]
			for j in range(m):
				A[i][j] = A[i][j] - A[k][j] * johnCharles
				printM(A)
				raw_input()
	#backwards now
	for k in range(n):
		for i in range(k+1, n):
			johnCharles = A[k][i]
			for j in range(m):
				A[k][j] = A[k][j] - A[i][j] * johnCharles
				printM(A)
				raw_input()
				
	for jc in range(n):
		I[jc] = A[jc][int(m/2):]
		
	print "I Matrix:"
	printM(I)
	
	return I
	

#Let's try this stuff out!
#testMatrix = [[2,3,1,5], [6,13,5,19], [2,19,10,23], [4,10,11,31]]
#equalsMatrix = [[8], [5], [3], [7]]

testMatrix2 = [[1, 5, 4], [2, 0, 3], [5, 8, 2]]
equalsMatrix2 = [[12], [9], [5]]

#identity = invert(testMatrix)
identity2 = invert(testMatrix2)

raw_input()
print "Solution matrix:"
#printM(mult(identity, equalsMatrix))
sol = mult(identity2, equalsMatrix2)
printM(sol)

raw_input()
print "Actual solution matrix:"
act = [[-3/19],[-1/19],[59/19]]
printM(act)

raw_input()
print "Difference:"
printM(sub(sol, act))

