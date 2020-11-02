if __name__ == "__main__":
    example_points = [[0/5], [3/2], [5/10]]

    # f(0) = a*0^2 + b*0 + c = 5
    # f(3) = a*3^2 + b*3 + c = 2
    # f(5) = a*5^2 + b*5 + c = 10

    matrix = [
        [example_points[0][0]**2, example_points[0][0], 1],
        [example_points[1][0]**2, example_points[1][0], 1],
        [example_points[2][0]**2, example_points[2][0], 1],
        [example_points[0][0], example_points[1][0], example_points[2][0]]
    ]

    print(matrix)