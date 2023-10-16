# Libraries
import curses

# Local modules
from .write import write
from .screens import getScreenText
from .colors import NORMAL_COLOR, SELECTED_COLOR


def init(window):
    """
    Initializes values and calls the home screen function.
    """
    curses.init_pair(NORMAL_COLOR, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(SELECTED_COLOR, curses.COLOR_BLACK, curses.COLOR_GREEN)
    boot(window)


def boot(window):
    """
    Gets the first screen and renders it.
    """
    write(window, getScreenText(0)) # Display the first screen
    window.getch()
