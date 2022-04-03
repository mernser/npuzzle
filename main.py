import argparse
from heuristics import *
from states_generator import *
from convertion import *
from astar import a_star, a_star_info, a_star_plot
from validate import *
from terminal_state import terminal_state_generator
from parse_args import parser_init
from classes import *


def main():
    args = parser_init(argparse.ArgumentParser(description="WELCOME TO PUZZLE SOLVER", add_help=False))
    input_puzzle = validate_puzzle(open_file(args.filename))
    size = len(input_puzzle)
    solved_state = terminal_state_generator(size, args.puzzle_type)
    state = state_selector(args.search_type)

    x, y = puzzle_to_coords(solved_state, size)
    puzzle_solved = state(g=0, h=0, x=x, y=y, puzzle=puzzle_to_list(solved_state))

    not_solved = get_solved(size=size, solved_x=puzzle_solved.x, solved_y=puzzle_solved.y)
    heuristic = get_heuristic(size=size, solved_x=puzzle_solved.x, solved_y=puzzle_solved.y,
                              heuristic_type=args.heuristic_type)
    states_generator = get_states_generator(heuristic=heuristic, size=size)

    x, y = puzzle_to_coords(input_puzzle, size)
    current_state = state(g=0, h=0, x=x, y=y, puzzle=puzzle_to_list(input_puzzle))
    current_state.h = heuristic(current_state.x, current_state.y)

    solvable(puzzle_solved, current_state, size)

    print(f"algorithm: {args.search_type}\n"
          f"puzzle type: {args.puzzle_type}\n"
          f"heuristic: {heuristic.__name__}\n"
          f"value: {current_state.f}\n",
          "_"*20, sep="")

    if args.info == "off":
        a_star(current_state, not_solved, states_generator, size, args)
    elif args.info == "text":
        a_star_info(current_state, not_solved, states_generator, size, args)
    elif args.info == "plot":
        a_star_plot(current_state, not_solved, states_generator, size, heuristic, args)


if __name__ == '__main__':
    main()
