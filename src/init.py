# Libraries
import curses

# Local modules
from .write import write


def init(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    boot(stdscr)


def boot(stdscr):
    write(stdscr, "Lorem ipsum dolor sit amet consectetur adipisicing elit.")
    stdscr.getch()
