import sys
import gui
import os
if sys.platform.__contains__("linux"):
    os.system("chmod 777 pkg_dec")

gui.vp_start_gui()
