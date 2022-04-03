from classes import Corners


def get_heuristic(size, solved_x, solved_y, heuristic_type):
    power = size ** 2
    if heuristic_type == "hamming":
        return get_hamming(power, solved_x, solved_y)
    elif heuristic_type == "manhattan":
        return get_manhattan(power, solved_x, solved_y)
    elif heuristic_type == "patterns":
        return get_patterns(power, solved_x, solved_y)
    elif heuristic_type == "corners":
        return get_corners(size, power, solved_x, solved_y)
    elif heuristic_type == "last_move":
        return get_last_move(size, power, solved_x, solved_y)
    elif heuristic_type == "conflicts":
        print("NOT IMPLEMENTED, SORRY MERNSER IS A LAZY BASTARD")
        exit()
        return get_conflicts(power, solved_x, solved_y)
    else:
        print("CHOOSE VALID HEURISTIC OPTION")
        exit()


def get_hamming(power, solved_x, solved_y):
    def hamming(current_x, current_y):
        distance = 0
        for i in range(1, power):
            if solved_x[i] != current_x[i] or solved_y[i] != current_y[i]:
                distance += 1
        return distance
    return hamming


def get_manhattan(power, solved_x, solved_y):
    def manhattan(current_x, current_y):
        distance = 0
        for i in range(1, power):
            distance += abs(solved_x[i] - current_x[i]) + abs(solved_y[i] - current_y[i])
        return distance
    return manhattan


def get_last_move(size, power, solved_x, solved_y):
    if solved_x[0] == 0 and solved_y[0] == 0:
        nums_to_be_on_space = [1, size]
    elif solved_x[0] == size - 1 and solved_y[0] == size - 1:
        nums_to_be_on_space = [power - 1, power - size]
    else:
        nums_to_be_on_space = [
            power - 1, power - 3, power - 5, power - 7]

    if len(nums_to_be_on_space) == 2 and nums_to_be_on_space[0] == 1:
        def last_move(current_x, current_y):
            distance = 0
            for i in range(1, power):
                distance += abs(solved_x[i] - current_x[i]) + abs(solved_y[i] - current_y[i])
            if distance == 0:
                return distance
            if current_x[nums_to_be_on_space[0]] != 0 and current_y[nums_to_be_on_space[1]] != 0:
                return distance + 2
            return distance
    elif len(nums_to_be_on_space) == 2:
        def last_move(current_x, current_y):
            distance = 0
            for i in range(1, power):
                distance += abs(solved_x[i] - current_x[i]) + abs(solved_y[i] - current_y[i])
            if distance == 0:
                return distance
            if current_x[nums_to_be_on_space[0]] != size - 1 and current_y[nums_to_be_on_space[1]] != size - 1:
                return distance + 2
            return distance
    else:
        print("last_move heuristic is designed for classic and reverse, using manhattan instead...")

        def last_move(current_x, current_y):
            distance = 0
            for i in range(1, power):
                distance += abs(solved_x[i] - current_x[i]) + abs(solved_y[i] - current_y[i])
            return distance
    return last_move


def get_corners(size, power, solved_x, solved_y):
    def corners(current_x, current_y):
        cornering = Corners(None, None, None, None)
        distance = 0
        for i in range(power):
            if i != 0:
                distance += abs(solved_x[i] - current_x[i]) + abs(solved_y[i] - current_y[i])
            if current_x[i] == 0 and current_y[i] == 0:
                if solved_x[i] != 0 or solved_y[i] != 0:
                    cornering.left_upper = 0
            elif current_x[i] == 0 and current_y[i] == size - 1:
                if solved_x[i] != 0 or solved_y[i] != size - 1:
                    cornering.left_lower = 0
            elif current_x[i] == size - 1 and current_y[i] == size - 1:
                if solved_x[i] != size - 1 or solved_y[i] != size - 1:
                    cornering.right_lower = 0
            elif current_x[i] == size - 1 and current_y[i] == 0:
                if solved_x[i] != size - 1 or solved_y[i] != 0:
                    cornering.right_upper = 0
        distance += check_corners(cornering=cornering, power=power, size=size,
                                  current_x=current_x, current_y=current_y,
                                  solved_x=solved_x, solved_y=solved_y)
        return distance
    return corners


def check_corners(cornering, current_x, current_y, power, size, solved_x, solved_y):
    distance = 0
    for i in range(power):
        if cornering.left_upper is not None:
            if current_x[i] == 1 and current_y[i] == 0:
                if solved_x[i] == 1 and solved_y[i] == 0:
                    cornering.left_upper += 1
            elif current_x[i] == 0 and current_y[i] == 1:
                if solved_x[i] == 0 and solved_y[i] == 1:
                    cornering.left_upper += 1
        if cornering.left_lower is not None:
            if current_x[i] == 0 and current_y[i] == size - 2:
                if solved_x[i] == 0 and solved_y[i] == size - 2:
                    cornering.left_lower += 1
            elif current_x[i] == 1 and current_y[i] == size - 1:
                if solved_x[i] == 1 and solved_y[i] == size - 1:
                    cornering.left_lower += 1
        if cornering.right_lower is not None:
            if current_x[i] == size - 1 and current_y[i] == size - 2:
                if solved_x[i] == size - 1 and solved_y[i] == size - 2:
                    cornering.right_lower += 1
            elif current_x[i] == size - 2 and current_y[i] == size - 1:
                if solved_x[i] == size - 2 and solved_y[i] == size - 1:
                    cornering.right_lower += 1
        if cornering.right_upper is not None:
            if current_x[i] == size - 1 and current_y[i] == 1:
                if solved_x[i] == size - 1 and solved_y[i] == 1:
                    cornering.right_upper += 1
            elif current_x[i] == size - 2 and current_y[i] == 0:
                if solved_x[i] == size - 2 and solved_y[i] == 0:
                    cornering.right_upper += 1
    if cornering.left_upper == 2:
        distance += 2
    if cornering.left_lower == 2:
        distance += 2
    if cornering.right_lower == 2:
        distance += 2
    if cornering.right_upper == 2:
        distance += 2
    return distance


def get_patterns(power, solved_x, solved_y):
    pattern_border = int(power / 2)

    def patterns(current_x, current_y):
        distance_first_pattern = 0
        distance_second_pattern = 0
        for i in range(1, pattern_border + 1):
            distance_first_pattern += abs(solved_x[i] - current_x[i]) + abs(solved_y[i] - current_y[i])
        for i in range(pattern_border - 1, power):
            distance_second_pattern += abs(solved_x[i] - current_x[i]) + abs(solved_y[i] - current_y[i])
        if distance_first_pattern > distance_second_pattern:
            return distance_first_pattern
        else:
            return distance_second_pattern
    return patterns


def get_solved(size, solved_x, solved_y):
    power = size ** 2

    def not_solved(current_x, current_y):
        for i in range(power):
            if solved_x[i] != current_x[i] or solved_y[i] != current_y[i]:
                return True
        return False
    return not_solved


def get_conflicts(power, solved_x, solved_y):
    def conflicts(current_x, current_y):
        distance = 0
        for i in range(1, power):
            distance += abs(solved_x[i] - current_x[i]) + abs(solved_y[i] - current_y[i])
        return distance
    return conflicts


def get_none_heuristic():
    def none_heuristic(current_x, current_y):
        return 0
    return none_heuristic
