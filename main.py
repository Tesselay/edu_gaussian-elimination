def to_one(matrix, row_num, col_num):
    multiplicator = 1 / matrix[row_num][col_num]
    for element in range(len(matrix[row_num])):
        matrix[row_num][element] *= multiplicator

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


def correct_pos(matrix, row_num):
    correct_row = None
    for element in range(len(matrix)):
        if matrix[element][row_num] == 1:
            correct_row = element
            break
    if correct_row is not None:
        swap_elements(matrix, row_num, correct_row)

    return matrix


if __name__ == "__main__":

    # EXAMPLE MATRIX
    # x + y + z = 3
    # x + 2y + 3z = 0
    # x + 3y + 4z = -2

    matrix = [
        [1, 2, 1, 3],
        [2, 2, 3, 0],
        [1, 3, 4, -2]
    ]

    print(matrix)

    for element in range(len(matrix)):
        if matrix[element][element] != 1:
            try:
                matrix = to_one(matrix, element, element)
            except ZeroDivisionError as e:
                pass

    if matrix[1][1] == matrix[1][0] and matrix[1][1] == matrix[0][1]:
        matrix = swap_elements(matrix, 1, 2)

    for element in range(len(matrix)):
        if matrix[element][element] == -1:
            for sub_element in range(len(matrix[element])):
                matrix[element][sub_element] *= -1

        # if matrix[element+1][element+1] == matrix[element+1][element] and matrix[element+1][element+1] == matrix[element][element+1]:
        #     matrix = swap_elements(matrix, element+1, element-1)

        if matrix[element][element] != 1:
            try:
                matrix = to_one(matrix, element, element)
            except ZeroDivisionError as e:
                pass

        try:
            matrix = nullify_column(matrix, element+1, element)
        except IndexError as e:
            matrix = nullify_column(matrix, 0, element)
        matrix = nullify_column(matrix, element-1, element)

    print(matrix)