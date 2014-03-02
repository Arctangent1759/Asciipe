import curses
import signal
import subprocess
import console
from time import sleep
from threading import Thread
import sys

cat = """
   ____
  (.   \\
    \  |
     \ |___(\--/)
   __/    (  . . )
  "'._.    '-.O.'
       '-.  \\ "|\\
          '.,,/'.,,mrf
"""
error_msg = "everything is good."

"""
addr = raw_input("IP address: ")
port = raw_input("Port: ")
ip = addr + ":" + port
"""

ip = "10.142.39.57:8008"
ip = "0.0.0.0:8008"
if len(sys.argv)>1:
    ip = sys.argv[1]

HEIGHT, WIDTH = 0, 0

class Window:
    def __init__(self, stdscr):
        self.scr = stdscr


def trim_nowrap(s, w, h):
    lines = s.split('\n')
    lines = lines[:h]
    for i in xrange(len(lines)):
        if len(lines[i]) > w:
            lines[i] = lines[i][:w]
    return '\n'.join(lines)


def trim(s, w, h):
    lines = s.split('\n')
    result = []
    display_height = 0
    for line in lines:
       display_height += len(line) / w
       if display_height + len(result) > h-1:
           break
       result.append(line)
    return '\n'.join(result)

def main(w):

    curses.noecho()
    curses.cbreak()
    w.keypad(1)
    curses.start_color()
    curses.curs_set(0)
    #ui = UI(w)

    w.nodelay(1)

    def handle(*args):
        w.erase()
        w.refresh()
        WIDTH, HEIGHT = console.getTerminalSize()

    signal.signal(signal.SIGWINCH, handle)

    handle()

    # initialize sound
    """
    try:
        subprocess.check_output(['python','get.py','-ip',ip,'sound'])
    except Exception as e:
        error_msg = str(e)
    """
    try:
        while True:
            w.erase()
            response = subprocess.check_output(
                    ['python','get.py','-ip', ip, 'frame'])
            HEIGHT, WIDTH = w.getmaxyx()
            w.addstr(0,0,trim(response, WIDTH, HEIGHT))
            w.refresh()
    except KeyboardInterrupt as e:
        error_msg = str(e)
    except Exception as e:
        error_msg = str(e)
    finally:
        w.keypad(0)
        curses.nocbreak()
        curses.echo()
        curses.endwin()
        print error_msg

if __name__ == '__main__':
    curses.wrapper(main)
