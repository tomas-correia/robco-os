import curses
import time
# import winsound


DELAY = 0.02


def write(window, text: str) -> None:
    """
    Prints given text at a steady speed in the terminal,
    while emitting a beeping sound. 
    """

    for char in text:
        window.addstr(char, curses.color_pair(1))
        window.refresh()
        time.sleep(DELAY)
        # winsound.Beep(500, DELAY) # The Beep function purposely delays the loop
