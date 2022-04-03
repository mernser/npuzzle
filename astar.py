from heapq import heappush as insert, heappop as extract_maximum
from printer import find_way
import matplotlib.pyplot as plt


def a_star(current_state, not_solved, states_generator, size, args):
    index = 0
    open_set = []
    closed_set = {}
    insert(open_set, (current_state.f, index, current_state))
    while not_solved(current_state.x, current_state.y):
        current_state = extract_maximum(open_set)[-1]
        if tuple(current_state.map) in closed_set:
            continue
        possible_new_states = states_generator(current_state, closed_set)
        for i in possible_new_states:
            index += 1
            insert(open_set, (i.f, index, i))
        closed_set[tuple(current_state.map)] = current_state
    print("Complexity in time:", len(closed_set))
    print("Complexity in size:", index)
    find_way(current_state, closed_set, size, args)


def a_star_info(current_state, not_solved, states_generator, size, args):
    index = 0
    open_set = []
    closed_set = {}
    insert(open_set, (current_state.f, index, current_state))
    while not_solved(current_state.x, current_state.y):
        current_state = extract_maximum(open_set)[-1]
        print(len(str(index)) * "_", current_state.map,
              f"g:{current_state.g}", f"h:{current_state.h}", f"f:{current_state.f}", "seeder")
        if tuple(current_state.map) in closed_set:
            continue
        possible_new_states = states_generator(current_state, closed_set)
        for i in possible_new_states:
            index += 1
            insert(open_set, (i.f, index, i))
            print(index, i.map, f"g:{i.g}", f"h:{i.h}", f"f:{i.f}")
        closed_set[tuple(current_state.map)] = current_state
    print("Complexity in time:", len(closed_set))
    print("Complexity in size:", index)
    find_way(current_state, closed_set, size, args)


def a_star_plot(current_state, not_solved, states_generator, size, heuristic, args):
    x = []
    y = []
    index = 0
    open_set = []
    closed_set = {}
    insert(open_set, (current_state.f, index, current_state))
    while not_solved(current_state.x, current_state.y):
        current_state = extract_maximum(open_set)[-1]
        if tuple(current_state.map) in closed_set:
            continue
        possible_new_states = states_generator(current_state, closed_set)
        for i in possible_new_states:
            index += 1
            insert(open_set, (i.f, index, i))
        x.append(current_state.g)
        y.append(heuristic(current_state.x, current_state.y))
        closed_set[tuple(current_state.map)] = current_state
    print("Complexity in time:", len(closed_set))
    print("Complexity in size:", index)
    find_way(current_state, closed_set, size, args)
    plt.scatter(x, y)
    plt.xlabel("steps")
    plt.ylabel("proximity")
    plt.title(f"a_star CIS:{index} CIT:{len(closed_set)}")
    plt.show()
