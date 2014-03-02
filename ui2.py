import curses
import signal
import subprocess
from time import sleep
from threading import Thread

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


class UI(Thread):
    DELAY = .1 #Refresh delay
    def __init__(self,stdscr):
        Thread.__init__(self)
        self.isRunning = False
        self.stdscr = stdscr

    def run(self):
        #Main loop
        self.isRunning = True
        while self.isRunning:
            self.height, self.width = self.stdscr.getmaxyx()
            self.stdscr.addstr(5,5,str((self.width, self.height)))
            self.stdscr.refresh()
            sleep(UI.DELAY)


    def stop(self):
        self.isRunning = False

def main(w):

    curses.noecho()
    curses.cbreak()
    w.keypad(1)
    curses.start_color()
    curses.curs_set(0)
    ui = UI(w)

    w.nodelay(1)
    dim = (0, 0)
    def handle(*args):
        w.erase()
        w.refresh()

    signal.signal(signal.SIGWINCH, handle)

    handle()
    try:
        while True:
            w.addstr(0,0,cat)
            w.refresh()
    except Exception as e:
        print e
    except KeyboardInterrupt as e:
        print "Bye!"
    finally:
        #ui.stop()
        w.keypad(0)
        curses.nocbreak()
        curses.echo()
        curses.endwin()

if __name__ == '__main__':
    curses.wrapper(main)
