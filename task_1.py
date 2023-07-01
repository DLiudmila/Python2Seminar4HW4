# Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # Создаем новую матрицу
    new_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    # Транспонируем матрицу
    for i in range(rows):
        for j in range(cols):
            new_matrix[j][i] = matrix[i][j]

    return new_matrix


transposed = transpose_matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(transposed)