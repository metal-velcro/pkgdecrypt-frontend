#! /usr/bin/env python
#
# Support module generated by PAGE version 4.8.9
# In conjunction with Tcl version 8.6
#    Mar 23, 2017 08:45:51 PM


import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1


def extract():
    print('gui_support.extract')
    sys.stdout.flush()

def input():
    print('gui_support.input')
    sys.stdout.flush()

def output():
    print('gui_support.output')
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import gui
    gui.vp_start_gui()


