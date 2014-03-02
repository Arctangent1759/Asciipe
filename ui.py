import curses
from time import sleep
from threading import Thread

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

try:
    s= curses.initscr()
    curses.noecho()
    curses.cbreak()
    s.keypad(1)
    curses.start_color()
    curses.curs_set(0)

    ui = UI(s)
    ui.start()

    sleep(15)

except Exception as e:
    print e
except KeyboardInterrupt as e:
    print "Bye!"
finally:
    ui.stop()

    s.keypad(0)
    curses.nocbreak();
    curses.echo()
    curses.endwin()
