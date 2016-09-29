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
__script__ = "PyHDDKeepAlive"
__version__ = "v0.1"
__git__ = "https://github.com/tf2manu994/PyHDDKeepAlive"

# Initiate rest of variables depending on OS
if os.name == "nt":
    WINDOWS = True
    ROOT_DIR = "C:\\"  # Used in help flag, as well as in default preferences
    ROOT_NAME = "C drive"  # Used in help flag
    DIR_SEPARATOR = "\\"
    EXAMPLE = "D:\\"
else:
    WINDOWS = False
    ROOT_DIR = "/"
    ROOT_NAME = "root directory"
    DIR_SEPARATOR = "/"
    EXAMPLE = "/mnt/disk1"

# Initiate variables
SLEEP = 55
VALID_ARGS = False
FILE_NAME = ".PyHDD"
PATH = ROOT_DIR


# Get command line arguments
for argument in sys.argv[1:]:
    # Get the first 7 characters of argument and check if they're "--path"
    if argument[:7] == "--sleep":
        try:
            # Ignore the 8th one because it's an equals, we don"t need that
            SLEEP = int(argument[8:])
            VALID_ARGS = True
        except ValueError:
            print('That\'s not a valid amount of time.')
            print('Make sure you wrote --sleep=NUMBER and not --sleep NUMBER?')
            sys.exit()

    elif argument[:6] == "--path":
        PATH = argument[7:]
        VALID_ARGS = True
        if SLEEP == 55:
            continue
        else:
            break
    elif argument == "help" or "-help" or "--help":
        print(__script__)
        print("The command line arguments you can use are:")
        print("--path=<Insert path to write to here> Default is %s" % ROOT_DIR)
        print("--sleep=<Seconds To Sleep>  Default is 55")
        print("For example, you might do --path=%s --sleep=30" % EXAMPLE)
        sys.exit()
    elif argument == "contact" or "copyright" or "author":
        print(__author__)
        print(__contact__)
        print(__website__)
        print(__script__, __version__)
        print(__git__)
        print("For help, run with the argument \"--help\"")
        sys.exit()
    else:
        print("No  valid arguments were given.")
        print("If you would like help, run with the argument \"--help\"")
        sys.exit()


if not PATH.endswith(DIR_SEPARATOR):
    PATH += DIR_SEPARATOR

if PATH == "C:\\":
    PATH = "C:\\temp\\"

FILE = PATH + FILE_NAME
if os.path.isfile(FILE):
    print("The file already exists.")
    print("To make sure I don\"t delete something important, I have stopped.")
    print("Please remove the file ", FILE)
else:
    print("Running at ", PATH, "every", SLEEP, "seconds!")
    # Sets what to write
    toWrite = ("%s %s by %s <%s>"
               % (__script__, __version__, __author__, __contact__))

    while True:
        try:
            # The writer creates the empty file that we can then write to.
            WRITER = open(FILE, "w")
            WRITER.write(toWrite)
            WRITER.close()
            os.remove(FILE)
            time.sleep(SLEEP)
        except PermissionError:
            print("Oops, we don't have access to that directory.")
            print("Try another directory on the same drive.")
            sys.exit()
        except KeyboardInterrupt:
            print("Stopping...")
            if os.path.isfile(FILE):
                print("Deleting %s" % FILE)
                os.remove(FILE)
                sys.exit()
            else:
                print("Done!")
                sys.exit()
