import curses
import time

DELAY = 0.02

def write(screen, text):
    for char in text:
        screen.addstr(char, curses.color_pair(1))
        screen.refresh()
        time.sleep(DELAY)
