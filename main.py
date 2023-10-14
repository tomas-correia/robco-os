import curses

from src.init import init

curses.wrapper(init)
