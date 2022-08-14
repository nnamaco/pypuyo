import numpy as np
from math import floor
from random import choice
from copy import deepcopy


class Game:
    class _Puyo:
        def __init__(self, x, y, color):
            self.x = x
            self.y = y
            self.color = color

        def get_x(self):
            return self.x

        def get_y(self):
            return self.y

        def get_color(self):
            return self.color

        def set_x(self, val):
            self.x = val

        def set_y(self, val):
            self.y = val

    def __init__(self, width=5, height=13, frames_to_fall=1, types=("Red", "Blue", "Yellow", "Green", "Purple")):
        self.width = width
        self.height = (height + 2)
        self.board = np.full((self.height, self.width), None, dtype=object)
        self.next_spin = None
        self.next_move = None
        self.frames_to_fall = frames_to_fall
        self.frame_count = 1
        self.colors = types
        self.falling_puyos = [None, None]
        self.dirs_tf = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.dir_ = None
        self.is_gameover = False
        self.highest_y = (self.height - 2)

    def is_over(self):
        return self.is_gameover

    def get(self):
        tmp_list = deepcopy(self.board)
        for puyo in self.falling_puyos:
            if puyo is not None:
                if (puyo.get_x() in range(self.width))\
                        and (puyo.get_y() in range(self.height)):
                    tmp_list[puyo.get_y()][puyo.get_x()] = puyo.get_color()
        return tmp_list[2:]

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height-2

    def get_types(self):
        return self.colors

    def spin_left(self):
        self.next_spin = "l"

    def spin_right(self):
        self.next_spin = "r"

    def move_left(self):
        self.next_move = "l"

    def move_right(self):
        self.next_move = "r"

    def update(self):
        # spin
        if (self.next_spin is not None) and (None not in self.falling_puyos):
            center_x = self.falling_puyos[0].get_x()
            center_y = self.falling_puyos[0].get_y()
            if self.next_spin == 'l':
                if self.dir_ >= 3:
                    self.dir_ = 0
                else:
                    self.dir_ += 1
            elif self.next_spin == 'r':
                if self.dir_ <= 0:
                    self.dir_ = 3
                else:
                    self.dir_ -= 1
            if ((center_x + self.dirs_tf[self.dir_][0]) in range(self.width))\
                    and ((center_y + self.dirs_tf[self.dir_][1]) in range(self.height))\
                    and ((self.board[center_y + self.dirs_tf[self.dir_][1]][center_x + self.dirs_tf[self.dir_][0]]) == None):
                self.falling_puyos[1].set_x(center_x + self.dirs_tf[self.dir_][0])
                self.falling_puyos[1].set_y(center_y + self.dirs_tf[self.dir_][1])
            self.next_spin = None
        # move
        if (self.next_move is not None) and (self.falling_puyos != (None, None)):
            no = [True, True]
            if self.next_move == 'r':
                add = 1
            elif self.next_move == 'l':
                add = -1
            for i, puyo in enumerate(self.falling_puyos):
                if puyo is not None:
                    puyo.set_x(puyo.get_x() + add)
                    if (puyo.get_x() in range(self.width)) and (self.board[puyo.get_y()][puyo.get_x()] == None):
                        no[i] = False
                else:
                    no[i] = False
            if True in no:
                for puyo in self.falling_puyos:
                    if puyo is not None:
                        puyo.set_x(puyo.get_x() - add)
            self.next_move = None
        # fall
        if self.frame_count == self.frames_to_fall:
            if None not in self.falling_puyos:
                self.falling_puyos.sort(key=lambda x: x.get_y(), reverse=True)
            for i, puyo in enumerate(self.falling_puyos):
                if puyo is not None:
                    add = 0
                    if None not in self.falling_puyos:
                        if (self.dirs_tf[self.dir_][1] != 0)\
                                and (min(self.falling_puyos[0].get_y(), self.falling_puyos[1].get_y()) == puyo.get_y()):
                            add = 1
                    if ((puyo.get_y() + (add + 2)) <= self.height) and (self.board[puyo.get_y() + 1][puyo.get_x()] == None):
                        puyo.set_y(puyo.get_y() + 1)
                    else:
                        if puyo.get_y() <= -1:
                            self.is_gameover = True
                        if puyo.get_y() < self.highest_y:
                            self.highest_y = puyo.get_y()
                        self.board[puyo.get_y()][puyo.get_x()] = puyo.get_color()
                        self.falling_puyos[i] = None
            if self.falling_puyos == [None, None]:
                self.falling_puyos = [self._Puyo(floor(self.width / 2), 1, choice(self.colors)),
                                      self._Puyo(floor(self.width / 2), 0, choice(self.colors))
                                     ]   
                self.dir_ = 2
            keep_finding = True
            while keep_finding == True:
                # puyo-dropping
                for y, list_ in enumerate(self.board[:(self.highest_y - 1):-1]):
                    true_y = self.height - (y + 1)
                    if np.all(self.board[(self.highest_y - 1):(true_y + 1)] == None):
                        self.highest_y = (true_y + 1)
                        break
                    else:
                        for x, color in enumerate(list_):
                            if color == None:
                                self.board[true_y][x], self.board[true_y - 1][x] = self.board[true_y - 1][x], self.board[true_y][x]
                # puyo-disapearing
                targets = {color: [] for color in self.colors}
                for y, list_ in enumerate(self.board[self.highest_y:]):
                    for x, color in enumerate(list_):
                        if color is not None:
                            target = []
                            def _find(x, y ,list):
                                list.append((x, y))
                                for direction in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                                    find_x = x + direction[0]
                                    find_y = y + direction[1]
                                    if (find_x in range(self.width)) and (find_y in range(self.height)):
                                            if ((find_x, find_y) not in list) and (self.board[find_y][find_x] == self.board[y][x]):
                                                _find(find_x, find_y, list)
                            _find(x, (y + self.highest_y), target)
                            target.sort(key=lambda x: x[0] + (x[1] * 100))
                            if (len(target) >= 4) and (target not in targets[color]):
                                targets[color].append(target)
                erase_count = 0
                for color_list in targets.values():
                    if len(color_list) > 0:
                        for target in color_list:
                            for tf in target:
                                erase_count += 1
                                self.board[tf[1]][tf[0]] = None
                if erase_count == 0:
                    keep_finding = False
            self.frame_count = 1
        else:
            self.frame_count += 1
