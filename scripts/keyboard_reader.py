#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

import curses
import threading
import time

pub = {}
lock = threading.Event()

def keyboard_listener(stdscr):
    # don't wait for input when calling getch
    stdscr.nodelay(1)
    # hide the cursor
    curses.curs_set(0)

    stdscr.addstr('Reading keyboard... (Press Esc to exit)')

    c = -1
    while c != 27 and lock.isSet():
        # get keyboard input, returns -1 if none available
        c = stdscr.getch()
        if c != -1:
            # return curser to start position
            stdscr.move(1, 0)

            # print numeric value
            try:
                stdscr.addstr('key: ' + chr(c) + '   ')
            except:
                stdscr.addstr('key: ??   ')

            stdscr.move(2, 0)
            stdscr.addstr(' id: ' + str(c) + '   ')

            pub.publish(c)

            stdscr.refresh()

def read_keyboard():
    curses.wrapper(keyboard_listener)


if __name__ == '__main__':

    # Init ROS
    rospy.init_node('read_keyboard')

    # Clear the lock when a shutdown request is recieved
    rospy.on_shutdown(lock.clear)

    # Init publisher
    pub = rospy.Publisher('keyboard', Int32, queue_size=10)

    # Read keyboard
    try:
        lock.set()
        t = threading.Thread(target=read_keyboard)
        t.start()
    except KeyboardInterrupt:
        lock.clear()
    except rospy.ROSInterruptException:
        lock.clear()

