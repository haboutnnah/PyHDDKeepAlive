#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
PyHDDKeepAlive v0.1 by Manmeet Gill
© Manmeet Gill 2016
https://manmeetgill.com
contact@manmeetgill.com
https://github.com/tf2manu994/PyHDDKeepAlive
"""
import sys  # Used for getting command line arguments
import os  # Used to delete file after creation
import time  # Used to make sure the program doesn't loop endlessly and max your CPU
__author__ = "Manmeet Gill"
__contact__ = "contact@manmeetgill.com"
__website__ = "https://manmeetgill.com"
__name__ = "PyHDDKeepAlive"
__version__ = "v0.1"
__git__ = "https://github.com/tf2manu994/PyHDDKeepAlive"
# Initiate variables
sleep = 55
validArgs = False
fileName = ".PyHDD"
# Initiate rest of variables depending on OS
if os.name == "nt":
    win = True
    rootDir = "C:\\"  # Used in help flag, as well as in default preferences
    rootName = "C drive"  # Used in help flag
    dirSeparator = "\\"
else:
    win = False
    rootDir = "/"
    rootName = "root directory"
    dirSeparator = "/"
path = rootDir


def complain():
    print("No  valid arguments were given, assuming to run at ", rootDir)  # Yell at end user
    print("If you would like help, run with argument --help")  # They didn't follow readme, they deserve it

# Get command line arguments
for arg in sys.argv[1:]:
    if arg[:7] == "--sleep":
        try:
            sleep = int(arg[8:])
            validArgs = True
        except ValueError:
            print('That\s not a valid amount of time.')
            print('Did you make sure you wrote --sleep=NUMBER and not --sleep NUMBER?')
            sys.exit()
    elif arg[:6] == "--path":  # Get the first 6 characters of argument and check if they're "--path"
        path = arg[7:]  # Ignore the 7th one because it's an equals, we don"t need that
        validArgs = True
        if sleep == 55:
            continue
        else:
            break
    elif arg == "help" or "\-help" or "\-\-help":
        print("The command line arguments you can use are --path=Path and --sleep=SecondsToSleep")
        print("Make sure to replace Path and SecondsToSleep with values.")
        print("Their defaults are your ", rootName, " and 55 seconds, respectively.")
        print("For instance, if you run with --path=", rootDir, ", it will run on your", rootName, ".")
        print("You can also specify where you want your temp file to go, by entering the full path.")
        print("If you want the temp file to go in ", rootDir, "temp, you can use --path=", rootDir, "temp.")
        print("If you want it to sleep for more or less than 55 seconds, use the --sleep argument.")
        sys.exit()
    elif arg == "contact" or "copyright" or "author":
        print(__author__)
        print(__contact__)
        print(__website__)
        print(__name__, __version__)
        print(__git__)
        sys.exit()
    else:
        complain()


if not path.endswith(dirSeparator):
    path += dirSeparator

if path == "C:\\":
    path = "C:\\temp\\"

file = path + fileName
if os.path.isfile(file):
    print("The file already exists. To make sure I don\"t delete something important, I have stopped.")
    print("Please remove the file ", file)
else:
    print("Running at ", path, "every", sleep, "seconds!")
    toWrite = __name__ + __version__ + "by " + __author__ + "<" + __contact__ + ">"
    while True:
        try:
            writer = open(file, "a")
            writer.write(toWrite)
            writer.close()
            os.remove(file)
            time.sleep(sleep)
        except PermissionError:
            print("Oops, we don't have access to that directory. Try another directory on the same drive.")
        except KeyboardInterrupt:
            print("Stopping...")
            if os.path.isfile(file):
                print("Deleting " + file)
                os.remove(file)
            else:
                print("Done!")
