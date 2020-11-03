def to_one(matrix):
    multiplicator = 1 / matrix[0][0]
    for element in range(len(matrix[0])):
        matrix[0][element] *= multiplicator

    return matrix


def nullify_column(matrix, row_num, col_num):
    nullifier = matrix[row_num][col_num]
    for element in range(len(matrix[row_num])):
        matrix[row_num][element] = matrix[row_num][element] - nullifier * matrix[col_num][element]

    return matrix


def sign_reverse(matrix, row_num):
    sign_reverse = -1
    for element in range(len(matrix[row_num])):
        matrix[row_num][element] = matrix[row_num][element] * sign_reverse

    return matrix


def swap_elements(list, pos_1, pos_2):
    list[pos_1], list[pos_2] = list[pos_2], list[pos_1]

    return list



if __name__ == "__main__":

    # EXAMPLE MATRIX
    # x + y + z = 3
    # x + 2y + 3z = 0
    # x + 3y + 4z = -2

    matrix = [
        [1, 1, 1, 3],
        [1, 2, 3, 0],
        [1, 3, 4, -2]
    ]

    correct_row = None
    for element in range(len(matrix)):
        if matrix[element][0] == 1:
            correct_row = element
            break
    if correct_row is not None:
        swap_elements(matrix, 0, correct_row)

    correct_row = None
    for element in range(len(matrix)):
        if matrix[element][1] == 1:
            correct_row = element
            break
    if correct_row is not None:
        swap_elements(matrix, 1, correct_row)

    correct_row = None
    for element in range(len(matrix)):
        if matrix[element][2] == 1:
            correct_row = element
            break
    if correct_row is not None:
        swap_elements(matrix, 2, correct_row)

    print(matrix)

    matrix = to_one(matrix)

    matrix = nullify_column(matrix, 1, 0)
    matrix = nullify_column(matrix, 2, 0)

    matrix = nullify_column(matrix, 0, 1)
    matrix = nullify_column(matrix, 2, 1)

    matrix = sign_reverse(matrix, 2)

    matrix = nullify_column(matrix, 0, 2)
    matrix = nullify_column(matrix, 1, 2)

    print(matrix)