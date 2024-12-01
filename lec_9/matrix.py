import random

class Matrix:
    def __init__(self,rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = [[random.randint(1,15) for _ in range (cols)] for _ in range(rows) ]

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])
    
    def __add__(self, matrix2):
        if self.rows != matrix2.rows or self.cols != matrix2.cols:
            raise ValueError("Input correct matrices" )
        result = Matrix (self.rows,self.cols)
        result.matrix = [[self.matrix[i][j] + matrix2.matrix[i][j] for j in range(self.cols)] for i in range (self.rows)]
        return result

    def __sub__(self, matrix2):
        if self.rows != matrix2.rows or self.cols != matrix2.cols:
            raise ValueError("Input correct matrices" )
        result = Matrix (self.rows,self.cols)
        result.matrix = [[self.matrix[i][j] - matrix2.matrix[i][j] for j in range(self.cols)] for i in range (self.rows)]
        return result

    def __mul__(self, matrix2):
        if self.cols != matrix2.rows:
            raise ValueError ("Input correct matrices ")
        result = Matrix(self.rows, matrix2.cols)
        result.matrix = [[sum(self.matrix[i][k] * matrix2.matrix[k][j] for k in range(self.cols)) for j in range(matrix2.rows)]for i in range(self.rows)]
        return result

if __name__ == "__main__":
    mat1 = Matrix(3, 3)
    mat2 = Matrix(3, 3)

    
    print("Matrix 1:")
    print(mat1)
    print("\nMatrix 2:")
    print(mat2)

    print("\nMatrix 1 + Matrix 2:")
    print(mat1 + mat2)

    print("\nMatrix 1 - Matrix 2:")
    print(mat1 - mat2)

    mat3 = Matrix(3, 2)
    mat4 = Matrix(2, 3)
    print("\nMatrix 3:")
    print(mat3)
    print("\nMatrix 4:")
    print(mat4)
    print("\nMatrix 3 * Matrix 4:")
    print(mat3 * mat4)
