def state_selector(search):
    if search == 'greedy':
        return StateGreedy
    elif search == 'uniform_cost':
        return StateUniform
    else:
        return State


class State:
    def __init__(self, g, h, x, y, puzzle):
        self.g = g
        self.h = h
        self._f = 0
        self.x = x
        self.y = y
        self.move = 0
        self.map = puzzle

    @property
    def f(self):
        return self.g + self.h


class StateUniform:
    def __init__(self, g, h, x, y, puzzle):
        self.g = g
        self.h = h
        self._f = 0
        self.x = x
        self.y = y
        self.move = 0
        self.map = puzzle

    @property
    def f(self):
        return self.g


class StateGreedy:
    def __init__(self, g, h, x, y, puzzle):
        self.g = g
        self.h = h
        self._f = 0
        self.x = x
        self.y = y
        self.move = 0
        self.map = puzzle

    @property
    def f(self):
        return self.h


class Corners:
    def __init__(self, lu, ll, rl, ru):
        self.left_upper = lu
        self.left_lower = ll
        self.right_lower = rl
        self.right_upper = ru
