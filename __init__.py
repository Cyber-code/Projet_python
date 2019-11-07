import time
import curses


def main(stdscr):
    # disable cursor blinking
    curses.curs_set(0)

    # write something on the screen
    stdscr.addstr(5, 10, "Hello, world!")

    # update the screen
    stdscr.refresh()

    # wait for 3 seconds
    time.sleep(3)

    # clear the screen
    stdscr.clear()

    while 1:
        key = stdscr.getch()

        # clear existing texts
        stdscr.clear()

        if key == curses.KEY_UP:
        	stdscr.addstr(0, 0, "You pressed Up key!")
        elif key == curses.KEY_DOWN:
        	stdscr.addstr(0, 0, "You pressed Down key!")
        elif key == curses.KEY_ENTER or key in [10, 13]:
        	stdscr.addstr(0, 0, "You pressed Enter.")
        else:
        	break

        # update screen
        stdscr.refresh()



curses.wrapper(main)