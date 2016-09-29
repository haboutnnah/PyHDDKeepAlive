#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
PyHDDKeepAlive v0.1 by Manmeet Gill
© Manmeet Gill 2016
https://manmeetgill.com
contact@manmeetgill.com
https://github.com/tf2manu994/PyHDDKeepAlive
"""
# Used for getting command line arguments
import sys
# Used to delete file after creation
import os
# Used to make sure the program doesn't loop endlessly and max your CPU
import time

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
    example = "D:\\"
else:
    win = False
    rootDir = "/"
    rootName = "root directory"
    dirSeparator = "/"
    example = "/mnt/disk1"
path = rootDir


def complain():
    print("No  valid arguments were given, assuming to run at ", rootDir)
    print("If you would like help, run with the argument \"--help\"")


# Get command line arguments
for arg in sys.argv[1:]:
    # Get the first 7 characters of argument and check if they're "--path"
    if arg[:7] == "--sleep":
        try:
            # Ignore the 8th one because it's an equals, we don"t need that
            sleep = int(arg[8:])
            validArgs = True
        except ValueError:
            print('That\s not a valid amount of time.')
            print('Make sure you wrote --sleep=NUMBER and not --sleep NUMBER?')
            sys.exit()

    elif arg[:6] == "--path":
        path = arg[7:]
        validArgs = True
        if sleep == 55:
            continue
        else:
            break
    elif arg == "help" or "\-help" or "\-\-help":
        print("The command line arguments you can use are:")
        print("--path=<Insert path to write to here> Default is", rootDir)
        print("--sleep=<Seconds To Sleep>  Default is 55")
        print("For example, you might do --path=", example, "--sleep=30")
        sys.exit()
    elif arg == "contact" or "copyright" or "author":
        print(__author__)
        print(__contact__)
        print(__website__)
        print(__name__, __version__)
        print(__git__)
        print("For help, run with the argument \"--help\"")
        sys.exit()
    else:
        complain()

if not path.endswith(dirSeparator):
    path += dirSeparator

if path == "C:\\":
    path = "C:\\temp\\"

file = path + fileName
if os.path.isfile(file):
    print("The file already exists.")
    print("To make sure I don\"t delete something important, I have stopped.")
    print("Please remove the file ", file)
else:
    print("Running at ", path, "every", sleep, "seconds!")
    # Sets what to write
    toWrite = (__name__ + __version__
               + "by " + __author__ +
               "<" + __contact__ + ">")

    while True:
        try:
            writer = open(file, "a")
            writer.write(toWrite)
            writer.close()
            os.remove(file)
            time.sleep(sleep)
        except PermissionError:
            print("Oops, we don't have access to that directory.")
            print("Try another directory on the same drive.")
        except KeyboardInterrupt:
            print("Stopping...")
            if os.path.isfile(file):
                print("Deleting " + file)
                os.remove(file)
                sys.exit()
            else:
                print("Done!")
                sys.exit()
