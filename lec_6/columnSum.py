import random

def generateRandomMatrix(rows,cols):
    matrix = []
    for _ in range(rows):
        row = [random.randint(1,100) for _ in range(cols)]
        matrix.append(row)
    return matrix

def getColumnSum(matrix, colIndex):
    sum = 0
    for row in matrix:
        sum += row[colIndex]
    return sum

def getRowAverage(matrix, rowIndex):
    row = matrix[rowIndex]
    return sum(row)/len(row)    

if __name__ == "__main__":
    matrix = generateRandomMatrix(4,4)
    print("The matrix is: ")
    for row in matrix:
        print (row)

    columnsSum = getColumnSum(matrix, 1)
    print(f"Sum of the column: {columnsSum}")

    rowAverage = getRowAverage(matrix, 2) 
    print(f"The average of the row: {rowAverage}")