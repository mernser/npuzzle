from copy import deepcopy


def get_states_generator(size, heuristic):
    limit = size - 1

    def states_generator(current_state, closed_set):
        states = []
        zero_x = current_state.x[0]
        zero_y = current_state.y[0]

        if zero_y > 0 and current_state.move != 6:
            state = deepcopy(current_state)
            num = state.map[state.x[0] + (state.y[0] - 1) * size]
            state.map[state.x[0] + state.y[0] * size] = num
            state.map[state.x[0] + (state.y[0] - 1) * size] = 0

            state.y[num] = state.y[0]
            state.y[0] = state.y[0] - 1

            state.h = heuristic(state.x, state.y)
            state.g += 1

            state.move = 12

            if tuple(state.map) not in closed_set:
                states.append(state)
        if zero_y < limit and current_state != 12:
            state = deepcopy(current_state)
            state.h = heuristic(state.x, state.y)
            num = state.map[state.x[0] + (state.y[0] + 1) * size]
            state.map[state.x[0] + state.y[0] * size] = num
            state.map[state.x[0] + (state.y[0] + 1) * size] = 0

            state.y[num] = state.y[0]
            state.y[0] = state.y[0] + 1
            state.h = heuristic(state.x, state.y)
            state.g += 1

            state.move = 6

            if tuple(state.map) not in closed_set:
                states.append(state)
        if zero_x > 0 and current_state.move != 3:
            state = deepcopy(current_state)
            num = state.map[state.x[0] - 1 + state.y[0] * size]
            state.map[state.x[0] + state.y[0] * size] = num
            state.map[state.x[0] - 1 + state.y[0] * size] = 0

            state.x[num] = state.x[0]
            state.x[0] = state.x[0] - 1

            state.h = heuristic(state.x, state.y)
            state.g += 1

            state.move = 9

            if tuple(state.map) not in closed_set:
                states.append(state)
        if zero_x < limit and current_state.move != 9:
            state = deepcopy(current_state)
            num = state.map[state.x[0] + 1 + state.y[0] * size]
            state.map[state.x[0] + state.y[0] * size] = num
            state.map[state.x[0] + 1 + state.y[0] * size] = 0

            state.x[num] = state.x[0]
            state.x[0] = state.x[0] + 1
            state.h = heuristic(state.x, state.y)
            state.g += 1

            state.move = 3

            if tuple(state.map) not in closed_set:
                states.append(state)
        return states
    return states_generator
