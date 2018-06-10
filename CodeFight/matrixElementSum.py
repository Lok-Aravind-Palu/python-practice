

def matrixElementsSum(matrix):
    a = len(matrix)
    b = len(matrix[0])

    for x in range(3):
        k = 0
        for y in range(4):
            if matrix[x][y] == 0:
                a = a-1
                for z in range(a):
                    k = x + 1
                    matrix[k][y] = 0




    for u in matrix:
        for v in u:
            print(v)

    sum = 0
    for x in matrix:
        for y in x:
            sum += y
    return sum



matrix = [[0, 1, 1, 2],
          [0, 5, 0, 0],
          [2, 0, 3, 3]]

print(matrixElementsSum(matrix))
