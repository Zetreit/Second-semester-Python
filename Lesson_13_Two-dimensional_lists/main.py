from matrix_operations import create_matrix, add_matrices

# Создание двух случайных матриц
matrix1 = create_matrix(10, 10)
matrix2 = create_matrix(10, 10)

# Вывод созданных матриц
print("Первая матрица:")
for row in matrix1:
    print(row)

print("\nВторая матрица:")
for row in matrix2:
    print(row)

# Сложение матриц
result_matrix = add_matrices(matrix1, matrix2)

# Вывод результирующей матрицы, если сложение прошло успешно
if result_matrix:
    print("\nРезультирующая матрица:")
    for row in result_matrix:
        print(row)
