# Filename: MatrixToolkit.py

def printM(M):
	for johnCharles in M:
		print johnCharles
	print ""
	
def printA(*args):
	for jc in args:
		print " "*len(jc)**2 + jc[1] + " "*(len(jc)**2+8),
	print ""
	for cj in range( len(args[0][0]) ):
		for jc in args:
			print str( jc[0][cj] ) + "        ",
		print ""
		
def sub(M,N):
	rows = len(M)
	cols = len(M[0])
	X = [[0]*cols]*rows
	for i in range(rows):
		for j in range(cols):
			X[i][j] = M[i][j] - N[i][j]
	return X
	
def sub2(M,N):
	rows = len(M)
	X = [[0]*rows]
	for i in range(rows):
		X[i] = M[i] - N[i]
	return X
		
#I stole this one.
#source: http://www.syntagmatic.net/matrix-multiplication-in-python/
def zero(m,n):
    # Create zero matrix
    new_matrix = [[0 for row in range(n)] for col in range(m)]
    return new_matrix
def mult(matrix1,matrix2):
    # Matrix multiplication
    if len(matrix1[0]) != len(matrix2):
        # Check matrix dimensions
        print 'Matrices must be m*n and n*p to multiply!'
    else:
        # Multiply if correct dimensions
        new_matrix = zero(len(matrix1),len(matrix2[0]))
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    new_matrix[i][j] += matrix1[i][k]*matrix2[k][j]
        return new_matrix	
        
def splitLU(A):
	n = len(A)
	
	#java equiv. to array = new int[n][n]...python is not always simpler
	L = [[0 for row in range(n)] for col in range(n)]
	U = [[0 for row in range(n)] for col in range(n)]
	
	#initialize I with 1s on the diagonal and 0s above the diagonal
	for jc in range(n):
		L[jc][jc] = 1.0
		for i in range(jc):
			L[jc][i] = A[jc][i]
	printM(L)
	for jc in range(n):
		for i in range(jc, n):
			U[jc][i] = A[jc][i]
			
	return L, U
	
def explodePI(pi):
	n = len(pi)
	PI = [[0 for row in range(n)] for col in range(n)]
	
	for jc in range(n):
		PI[jc][pi[jc]] = 1
	
	return PI
	

# End of MatrixToolkit
