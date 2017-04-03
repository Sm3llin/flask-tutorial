import sys

"""
The SGR parameters 30-37 selected the foreground color, while
40-47 selected the background color and 1 to make text bold (brighter)

Intensity |  0  |  1  |  2  |  3  |  4  |  5  |  6  |  7
   Normal |Black| Red |Green| Yel | Blue|Magen| Cyan|White

"""

RED         = "\033[1;31m"
BRIGHTRED   = "\033[31;1m"
BLUE        = "\033[1;34m"
CYAN        = "\033[1;36m"
GREEN       = "\033[0;32m"
RESET       = "\033[0;0m"
BOLD        = "\033[;1m"
REVERSE     = "\033[;7m"
BLACKNWHITE = "\033[30;47m"

COLORS = {'RED': RED,
          'BRIGHTRED':  BRIGHTRED,
          'BLUE': BLUE,
          'CYAN': CYAN,
          'GREEN': GREEN,
          'RESET': RESET,
          'BOLD': BOLD,
          'REVERSE': REVERSE,
          'BLACKNWHITE': BLACKNWHITE}


class ConsoleColor:
    def __init__(self, color):
        if isinstance(color, str):
            color = COLORS[color.upper()]
        self.COLOR = color

    def __enter__(self):
        sys.stdout.write(self.COLOR)

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.write(RESET)


def set_color(color):
    return ConsoleColor(color)


def get_color(color):
    if isinstance(color, str):
        return COLORS[color.upper()]
