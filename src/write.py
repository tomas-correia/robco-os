import curses
import winsound


DELAY = 20


def write(screen, text) -> None:
    """
    Prints given text at a steady speed in the terminal,
    while emitting a beeping sound. 
    """

    for char in text:
        screen.addstr(char, curses.color_pair(1))
        screen.refresh()
        winsound.Beep(500, DELAY) # The Beep function purposely delays the loop
