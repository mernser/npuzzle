def terminal_state_generator(size, puzzle_type):
    terminal_state = []
    if puzzle_type == 'reverse_classic':
        for rows in range(size):
            terminal_state.append([i for i in range(rows * size, rows * size + size)])
    elif puzzle_type == 'classic':
        for rows in range(size):
            terminal_state.append([i for i in range(rows * size + 1, rows * size + size + 1)])
        terminal_state[-1][-1] = 0
    else:
        terminal_state = [[0] * size for _ in range(size)]
        num = 1
        i = 0
        d = 0
        offset = -1
        total = size ** 2
        while num < total:
            offset += 1
            while i + offset < size - offset:
                terminal_state[d + offset][i + offset] = num
                num += 1
                i += 1
            i -= 1
            d += 1
            while d + offset < size - offset:
                terminal_state[d + offset][i + offset] = num
                num += 1
                d += 1
            d -= 1
            i -= 1
            while i + offset > offset:
                terminal_state[d + offset][i + offset] = num
                num += 1
                i -= 1
            while d + offset > offset:
                terminal_state[d + offset][i + offset] = num
                num += 1
                d -= 1
        if size % 2 == 0:
            terminal_state[d + 1 + offset][i + offset] = 0
    return terminal_state
