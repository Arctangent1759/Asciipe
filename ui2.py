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
error_msg = "everything is good."

"""
addr = raw_input("IP address: ")
port = raw_input("Port: ")
ip = addr + ":" + port
"""

ip = "10.142.39.57:8008"


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
    ui = UI(w)

    w.nodelay(1)

    def handle(*args):
        w.erase()
        w.refresh()

    signal.signal(signal.SIGWINCH, handle)

    handle()

    try:
        while True:
            w.erase()
            response = subprocess.check_output(
                    ['python','get.py','-ip', ip, 'frame'])
            height, width = w.getmaxyx()
            w.addstr(0,0,trim(response, width, height))
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
