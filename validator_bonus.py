import re
from main import terminal_state_generator, puzzle_to_list
import copy


def find_zero(state):
    """
    возвращает позицию нуля в строке
    """
    index = 0
    for i in state:
        if i == 0:
            return index
        index += 1
    print("\033[91mERROR: 0 is missing!\033[0m\nSTATE:", state)
    exit()


def checker(previous_state, current_state, power, size):
    """
    Перемещение 0 осуществляется только на 1 единицу в пределах строки, либо на длину строки при любых условиях
    Перемещение 0 на 1 требует дополнительной валидации, а именно был ли переход свершен в рамках строки
    Для этого проверяется является:
    если мы сместились левее - то стоит ли в начале строки место откуда пришли (% size == 0)
    если мы сместились правее - то стоит ли в начале новоей строки место куда пришли (% size == 0)
    """
    if len(current_state) is not power:
        print("\033[91mERROR: WRONG LEN SIZE\033[0m\nSTATE:", current_state,
              f"\nIS \033[91m{len(current_state)}\033[0m BUT SUPPOSE TO BE {power} LONG")
        exit()
    previous_state = copy.deepcopy(previous_state)
    previous_zero_pos = find_zero(previous_state)
    current_zero_pos = find_zero(current_state)
    previous_state[previous_zero_pos] = current_state[previous_zero_pos]
    previous_state[current_zero_pos] = 0
    if not previous_state == current_state:
        return False
    if abs(current_zero_pos - previous_zero_pos) == size:
        return True
    elif abs(current_zero_pos - previous_zero_pos) == 1:
        if current_zero_pos > previous_zero_pos and current_zero_pos % size == 0:
            return False
        elif current_zero_pos < previous_zero_pos and previous_zero_pos % size == 0:
            return False
        else:
            return True
    else:
        return False


def line_to_list(line):
    tmp = re.findall(r"\[.*\]", line)
    if not tmp:
        print('Huston, we have a problematic line!\nHere it is: {}'.format(line))
        exit()
    line = tmp[0]
    for i in ['[', ']', ',']:
        line = line.replace(i, '')
    line = [int(num) for num in line.split(' ')]
    return line


def validate_state(state, power):
    num = [i for i in range(power)]
    for i in num:
        c = state.count(i)
        if c > 1:
            print("number:", i, "is duplicated")
            return True
        elif c == 0:
            print("number:", i, "is missing")
            return True
        else:
            continue


def find_sol_line(file):
    index = 0
    sol = True
    for i in file:
        index += 1
        if "SOLUTION LENGTH:" in i:
            sol = False
            break
    if sol:
        print("Where is the SOLUTION LENGTH: substring goddammit?!")
        exit()
    return index


def open_file(filename):
    try:
        with open(filename, 'r') as f:
            file = f.readlines()
    except FileNotFoundError:
        print("INVALID FILE")
        exit()
    return file


def main():
    filename = input('\033[92mWelcome to Puzzle Solution Checker (PSC) from Mernsers Industries!\033[0m\n'
                     '\033[91mRestrictions:\033[0m Solution MUST go after "SOLUTION LENGTH:" line\n'
                     'Please enter filename\n')
    puzzle_type = input('..and puzzle type (snail[default], classic, reverse_classic)\n')
    file = open_file(filename)
    index = find_sol_line(file)
    previous_state = line_to_list(file[index])
    power = len(previous_state)
    size = int(power ** 0.5)
    if validate_state(previous_state, power):
        print("\033[91mINVALID INITIAL STATE\033[0m")
        exit()
    solved_state = puzzle_to_list(terminal_state_generator(size, puzzle_type=puzzle_type))
    if previous_state == solved_state:
        print("Movement: \033[92mOK\033[0m\nSolution: \033[92mFOUND\033[0m")
        exit()
    for line in file[index + 1::]:
        current_state = line_to_list(line)
        if checker(previous_state, current_state, power, size):
            pass
        else:
            print("Movement: \033[91mINVALID MOVE\nfrom", previous_state, "\nto  ", current_state, "\033[0m")
            exit()
        if current_state == solved_state:
            print("Movement: \033[92mOK\033[0m\nSolution: \033[92mFOUND\033[0m")
            exit()
        previous_state = current_state

    print("Movement: \033[93mOK\033[0m\nSolution: \033[91mNOT FOUND\033[0m")
    print("Terminal State is to be found:", solved_state)


if __name__ == '__main__':
    main()
