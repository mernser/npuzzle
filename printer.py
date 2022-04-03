import copy

from visualization import Visualization


def print_puzzle(puzzle, title="standart"):
    print(title)
    for i in puzzle:
        print(i)


def print_indecies(puzzle):
    size = len(puzzle)
    for i in range(size):
        print('')
        for d in range(size):
            print(i, d, sep=',', end=' ')


def print_solution_previous(current_state):
    to_print = []
    tmp = current_state
    while tmp:
        to_print.append(tmp)
        tmp = tmp.previous_map
    for i in to_print[::-1]:
        print(i.map, i.g, i.h, i.f, sep=' ')
    print("path:", len(to_print))


def print_solution(current_state, closed_set):
    to_print = []
    tmp = current_state
    while tmp:
        to_print.append(tmp)
        tmp = closed_set[tmp]
    for i in to_print[::-1]:
        print(i.map, i.g, i.h, i.f, sep=' ')
    print("path:", len(to_print))


def find_way(current_state, closed_set, size, args):
    moves = 0
    solution = [current_state]
    res = []
    state = copy.deepcopy(current_state)
    while state.move:
        moves += 1
        res.append(copy.deepcopy(state))
        if state.move == 12:
            num = state.map[state.x[0] + (state.y[0] + 1) * size]
            state.map[state.x[0] + state.y[0] * size] = num
            state.map[state.x[0] + (state.y[0] + 1) * size] = 0

        elif state.move == 6:
            num = state.map[state.x[0] + (state.y[0] - 1) * size]
            state.map[state.x[0] + state.y[0] * size] = num
            state.map[state.x[0] + (state.y[0] - 1) * size] = 0

        elif state.move == 9:
            num = state.map[state.x[0] + 1 + state.y[0] * size]
            state.map[state.x[0] + state.y[0] * size] = num
            state.map[state.x[0] + 1 + state.y[0] * size] = 0

        elif state.move == 3:
            num = state.map[state.x[0] - 1 + state.y[0] * size]
            state.map[state.x[0] + state.y[0] * size] = num
            state.map[state.x[0] - 1 + state.y[0] * size] = 0
        solution.append(state)
        state = closed_set[tuple(state.map)]
    if moves != 0:
        res.append(closed_set[tuple(state.map)])
    if args.is_visualize and size <= 4:
        Visualization([current_state] if len(res) == 0 else res[::-1], size, args)
    elif args.is_visualize and size > 4:
        print("Visualization is supported only for puzzles with dimensions 3x3, 4x4")
        exit()
    else:
        print("SOLUTION LENGTH:", moves)
        for index, i in enumerate(solution[::-1]):
            print(i.map, end="")
            if index == moves:
                print("")
                break
            if i.move == 9:
                print("←")
            elif i.move == 3:
                print("→")
            elif i.move == 12:
                print("↑")
            elif i.move == 6:
                print("↓")
