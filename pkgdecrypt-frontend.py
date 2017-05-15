import getopt
import sys
import gui
import os

if sys.platform.__contains__('linux'):
    def openFolder(path):
        os.system('xdg-open "' + path + '"')


elif sys.platform.__contains__('win'):

    def openFolder(path):
        os.system('explorer.exe "' + path + '"')

if sys.platform.__contains__("linux"):
    os.system("chmod 777 pkg_dec")
opts, args = getopt.getopt(sys.argv[1:], 'x:y:')
try:
    if args[0] != "":
        print "Extracting " + args[0]
        if sys.platform.__contains__("linux"):
            os.system('./pkg_dec "' +args[0]+'" "'+args[0]+'-output"')
            os.remove("out.bin")
            openFolder(args[0]+'-output')
            sys.exit()
        elif sys.platform.__contains__("win"):
            os.system('pkg_dec.exe "' + args[0] + '" "' + args[0] + '-output"')
            os.remove("out.bin")
            openFolder(args[0] + '-output')
            sys.exit()
except IndexError:
    print "Loading GUI"


gui.vp_start_gui()
