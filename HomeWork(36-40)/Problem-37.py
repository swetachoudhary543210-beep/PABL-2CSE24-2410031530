def set_zeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    row_zero = [False] * rows
    col_zero = [False] * cols
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_zero[i] = True
                col_zero[j] = True
    
    for i in range(rows):
        for j in range(cols):
            if row_zero[i] or col_zero[j]:
                matrix[i][j] = 0
    
    return matrix

matrix = eval(input())
print(set_zeroes(matrix))
