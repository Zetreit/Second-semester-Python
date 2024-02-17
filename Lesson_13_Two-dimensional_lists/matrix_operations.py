import random

# Функция для создания матрицы заданного размера со случайными значениями
def create_matrix(rows, cols):
    return [[random.randint(-100, 100) for _ in range(cols)] for _ in range(rows)]

# Функция для сложения двух матриц
def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Ошибка: размерности матриц не совпадают")
        return None
    
    result_matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result_matrix.append(row)
    
    return result_matrix
