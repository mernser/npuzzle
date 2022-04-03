from convertion import puzzle_to_list
from copy import deepcopy


def validate_numbers(state, size):
    num = [i for i in range(size)]
    for i in num:
        c = state.count(i)
        if c > 1:
            print("number:", i, "is duplicated")
            exit()
        elif c == 0:
            print("number:", i, "is missing")
            exit()
        else:
            continue


def open_file(filename):
    try:
        with open(filename, 'r') as f:
            puzzle = f.readlines()
    except FileNotFoundError:
        print("INVALID FILE")
        exit()
    return puzzle


def find_size(puzzle):
    init_state = []
    flag = 1
    size = 0
    for i in puzzle:
        if i.startswith("#"):
            continue
        if flag:
            if i.strip(' \n\t\r').isnumeric() and ' ' not in i:
                size = int(i)
            elif i.count('#') == 1 and i.split('#')[0].isnumeric() and ' ' not in i:
                size = int(i.split('#')[0].replace(' ', ''))
            flag = 0
            if size > 2:
                continue
            else:
                print(f"INVALID SIZE INPUT IN LINE: {i}", end="")
                exit()
        init_state.append(i)
    return size, init_state


def validate_puzzle(puzzle):
    size, init_state = find_size(puzzle)
    if len(init_state) != size:
        print(f"PUZZLE SIZE MISMATCH: required {size} VS {len(init_state)}")
        exit()
    tmp = []
    for i in init_state:
        tmp.append(validate_line(i, size))
    validate_numbers(puzzle_to_list(tmp), size ** 2)
    return tmp


def validate_line(line, size):
    new = []
    if '#' in line:
        line = line.split('#')[0]
    line = line.split(' ')
    for i in line:
        c = i.strip(' \t\n\r')
        if c.isnumeric():
            new.append(int(c))
        elif c:
            print(f"PUZZLE CONTAINS INVALID CHARACTER IN LINE: {line}")
            exit()
    if len(new) != size:
        print(f"PUZZLE LINE SIZE MISMATCH: required {len(new)} VS {size}")
        exit()
    return new


def solvable(solved_state, current_state, size):
    if size % 2 == 1:
        if calculate_inversion(current_state) % 2 == calculate_inversion(solved_state) % 2:
            return
    else:
        if (calculate_inversion(solved_state) + which_row_zero(solved_state, size)) % 2 == \
                (calculate_inversion(current_state) + which_row_zero(current_state, size)) % 2:
            return
    print("PUZZLE UNSOLVABLE")
    exit()


def which_row_zero(current_state, size):
    return int(current_state.map.index(0) / size)


def calculate_inversion(puzz):
    puzzle = deepcopy(puzz.map)
    del puzzle[puzzle.index(0)]
    inversion = 0
    index = 0
    for i in puzzle:
        index += 1
        for c in puzzle[index::]:
            if i > c:
                inversion += 1
    return inversion
