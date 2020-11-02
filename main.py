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

    multiplicator = 1 / matrix[0][0]
    for element in range(len(matrix[0])):
        matrix[0][element] *= multiplicator

    for element in range(len(matrix[1])):
        matrix[1][element] = matrix[1][element] - 1 * matrix[0][element]

    for element in range(len(matrix[2])):
        matrix[2][element] = matrix[2][element] - 1 * matrix[0][element]


    for element in range(len(matrix[0])):
        matrix[0][element] = matrix[0][element] - 1 * matrix[1][element]

    for element in range(len(matrix[2])):
        matrix[2][element] = matrix[2][element] - 2 * matrix[1][element]


    for element in range(len(matrix[2])):
        matrix[2][element] = matrix[2][element] * -1


    for element in range(len(matrix[0])):
        matrix[0][element] = matrix[0][element] - -1 * matrix[2][element]

    for element in range(len(matrix[1])):
        matrix[1][element] = matrix[1][element] - 2 * matrix[2][element]




    # multiplicator = 1 / matrix[1][1]
    # for element in range(len(matrix[1])):
    #     matrix[1][element] *= multiplicator
    #
    # multiplicator = 1 / matrix[2][2]
    # for element in range(len(matrix[2])):
    #     matrix[2][element] *= multiplicator

    print(matrix)