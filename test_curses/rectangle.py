import curses
from curses import textpad


def main(stdscr):
    i = 0
    while 1:
        i += 1
        curses.curs_set(0)
        sh, sw = stdscr.getmaxyx()
        box = [[i,i], [sh-3, sw-3]]
        textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
        stdscr.getch()


curses.wrapper(main)