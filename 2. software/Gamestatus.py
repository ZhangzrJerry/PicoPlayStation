from enum import Enum


class Gamestatus(Enum):
    win = 1
    end = 2
    left = 3
    right = 4
    up = 5
    down = 6
    double_left = 7
    double_right = 8
    double_up = 9
    double_down = 10
    home = 11
    game = 12