# Function that takes a matrix and a set of vectors and tests that they can be multiplied before performing the multiplication
def multiplyMatrixAndVectors(matrix, shape):
    bad = 0

    for i in shape:
        if not len(i) == len(matrix[0]):
            bad = 1
    for i in range(len(matrix)):
        if len(matrix)-1 == i:
            break
        if not len(matrix[i]) == len(matrix[i+1]):
            bad = 1
    for i in range(len(shape)):
        if not len(shape[i]) == 2:
            bad = 1

    newShape = []
    tempVector = []

    if bad == 0:
        for i, vector in enumerate(shape):
            tempVector = []
            #print(i, vector)
            x = vector[0]
            y = vector[1]
            #print('x',x,'y',y)
            for p in matrix:
                tempVector.append(p[0]*x + p[1]*y)
                #print(p, p[0]*x + p[1]*y, tempVector)
            newShape.append(tempVector)
            #print('newShape',newShape)
    return newShape

def displayMatrix(matrix):
    print('matrix')
    for i in matrix:
        print(i[0], i[1])

def displayShape(shape):
    print('shape')
    for i in shape:
        print('x', i[0], 'y', i[1])

def main():
    shape1 = [[4, 2],[1, 1]]
    matrix1 = [[-2, 0],[0, -2]]

    displayMatrix(matrix1)
    displayShape(shape1)
    displayShape(multiplyMatrixAndVectors(matrix1, shape1))

main()