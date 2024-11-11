def fill_matrix_vertically(n, m):
    matrix = [[0] * m for _ in range(n)]  
    value = 1  

    for j in range(m):
        for i in range(n):
            matrix[i][j] = j*len(matrix)+i+1
            value += 1  

    return matrix


def fill_matrix_horizontally(n, m):
    matrix = [[0] * m for _ in range(n)]  
    value = 1  

    for i in range(n):
        for j in range(m):
            matrix[i][j] = i*len(matrix[0]) + j + 1
            value += 1 

    return matrix


def fill_matrix(flag,n,m):
    matrix = [[0] * m for _ in range(n)]  
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = i*len(matrix[0]) + j + 1 if flag=="h" else j*len(matrix)+i+1
    return matrix

result = fill_matrix(flag="v",n=3,m=4)
for row in result:
    print(row)



