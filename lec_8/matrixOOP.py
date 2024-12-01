import random

class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[random.randint(1,20) for _ in range(m)] for _ in range(n)]

    def printMatrix(self):
        for row in self.matrix:
            print(row)
        
    def meanOfMatrix(self):
        totalSum = sum(sum(row) for row in self.matrix)
        totalElements = self.m * self.n
        return (totalSum)/(totalElements)

    def rowSum(self, rowIndex):
        if 0 <= rowIndex <=self.n:
            return sum(self.matrix[rowIndex])
        else:
            raise IndexError("Row out of bounds")
    
    def columnAverage(self, columnIndex):
        if  0 <= columnIndex <= self.m:
            columnSum = sum(self.matrix[i][columnIndex] for i in range(self.n))
            return columnSum / self.n
        else:
            raise IndexError("Column out of bound")
        
    def subMatrix(self, col1, col2, row1, row2):
        if 0 <= row1<=row2 < self.n and 0<= col1<=col2 <self.m:
            submatrix = [row[col1:col2+1] for row in self.matrix[row1:row2+1]]
            for row in submatrix:
                print (row)
        else:
            raise IndexError("Row or Columns out of bounds")

if __name__ == "__main__":

    matirx = Matrix(4,5)

    print("The matrix is: ")
    matirx.printMatrix()

    print(f"\nThe mean of the matrix: {matirx.meanOfMatrix()}")    

    rowIndex = 2
    print(f"\nThe sum of the row {rowIndex} is {matirx.rowSum(rowIndex)}")

    colIndex = 3
    print(f"\nThe avarage of the column {colIndex} is { matirx.columnAverage(colIndex)}")

    print("\nThe submatrix is: ")
    matirx.subMatrix(1,3,1,3)