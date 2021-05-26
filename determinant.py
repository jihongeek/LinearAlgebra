def det(matrix : list):
    """
    행렬식
    """
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    result = 0
    for i in range(len(matrix)):        
        minorMatrix = []
        for j in range(len(matrix)):
            row = []
            for k in range(len(matrix)):
                if j+1 != 1 and k + 1 != i+1:
                    row.append(matrix[j][k])
            if len(row) > 0:
                minorMatrix.append(row)
        result += (-1) **(1+i+1) * matrix[0][i] * det(minorMatrix)
    return result

def cofactor(matrix : list, rowNum : int, colNum : int):
    """
    여인자 
    """
    minorMatrix = []
    for j in range(len(matrix)):
        row = []
        for k in range(len(matrix)):
            if j+1 != rowNum and k + 1 != colNum:
                row.append(matrix[j][k])
        if len(row) > 0:
            minorMatrix.append(row)
    return (-1) **(rowNum+colNum) * det(minorMatrix)
        



