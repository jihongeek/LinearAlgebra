import determinant
def gcd(m,n):
    while m % n != 0:
        m,n = n, (m%n)
    return n

def qMatrix(matrix : list): 
    """
    qMatrix(유리 행렬) 변환함수 
    """
    newQMatrix = matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if str(type(matrix[i][j])) == "<class 'int'>":
                newQMatrix[i][j] = (matrix[i][j],1)
    return newQMatrix
def transpose(matrix : list):
    """
    전치행렬 
    """
    transposedMatrix = [ [None] * len(matrix) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            transposedMatrix[j][i] = matrix[i][j]
    return transposedMatrix
def multiply(matrix1 : list, matrix2 : list):
    """
    행렬곱 
    """
    multipliedMatrix = [[0]*len(matrix2[0]) for _ in range(len(matrix1))] 
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix1)):
                multipliedMatrix[i][j] += (matrix1[i][k] * matrix2[k][j])
    return multipliedMatrix
def scalarMultiply(scalar, matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j] *= scalar
    return matrix

def inverse(matrix : list):
    cofactorMatrix = [[0]*len(matrix) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            cofactorMatrix[i][j] = determinant.cofactor(matrix,i,j)
    return scalarMultiply(determinant.det(matrix), transpose(cofactorMatrix))
