def puzzle_to_dict(puzzle, size):
    dct = {}
    for i in range(0, size):
        for d in range(0, size):
            dct[puzzle[i][d]] = [i, d]
    return dct


def list_to_tuple(puzzle):
    return tuple([tuple(i) for i in puzzle])


def puzzle_to_coords(puzzle, size):
    x = [0] * size ** 2
    y = [0] * size ** 2
    for i in range(0, size):
        for d in range(0, size):
            x[puzzle[i][d]] = d
            y[puzzle[i][d]] = i
    return x, y


def puzzle_to_list(puzzle):
    return [n for row in puzzle for n in row]
