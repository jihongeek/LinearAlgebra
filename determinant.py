def det(matrix : list):
    """
    행렬식
    """
    # matrix의 크기가 2일 경우 행렬식을 쉽게 계산할 수 있으므로 계산한 후 값 반환  
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
    result = 0
    for i in range(len(matrix)):        
        # 소행렬
        minorMatrix = []
        for j in range(len(matrix)):
            row = []
            for k in range(len(matrix)):
                # 만약 성분이 선택한 행(1행)의 성분의 열과 행에 속하지 않을 경우 소행렬 행에 추가 
                if j+1 != 1 and k + 1 != i+1:
                    row.append(matrix[j][k])
            # 만약 소행렬의 행에 성분이 한개라도 있다면 소행렬에 넣기 
            if len(row) > 0:
                minorMatrix.append(row)
        result += (-1) **(1+i+1) * matrix[0][i] * det(minorMatrix) # (부호값 * 선택한 행의 성분 * 소행렬식 값)의 합
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
        



