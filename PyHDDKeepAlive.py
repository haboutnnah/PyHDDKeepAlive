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
import os
import sys
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
    # Remove flag markers, we don't need to process those.
    argument = argument.replace("-", "")
    argument = argument.replace("/", "")
    # Get the first 5 characters of argument and check if they're "path"
    if argument[:5] == "sleep":
        try:
            # Ignore the 6th one because it's an equals, we don"t need that
            SLEEP = int(argument[6:])
            # Tell the loop that there were valid arguments, stop the edge case
            VALID_ARGS = True
        except ValueError:
            print('That\'s not a valid amount of time.')
            print('Make sure you wrote sleep=NUMBER and not sleep NUMBER')
            sys.exit()
    # Get the first 4 characters
    elif argument[:4] == "path":
        # Ignore the 4th one, its an equals and we don't care
        PATH = argument[5:]
        # Tell the loop that there were valid arguments, stop the edge case
        VALID_ARGS = True
    elif argument == "help":
        print(__script__)
        print("The command line arguments you can use are:")
        print("path=<Insert path to write to here>. Default is %s" % ROOT_DIR)
        print("sleep=<Seconds To Sleep>  Default is 55")
        print("For example, you might do path=%s sleep=30" % EXAMPLE)
        print(argument)
        sys.exit()
    elif argument == "contact" or "copyright" or "author" or "version":
        print(__author__)
        print(__contact__)
        print(__website__)
        print(__script__, __version__)
        print(__git__)
        print("For help, run with the argument \"help\"")
        sys.exit()
    else:
        print("No  valid arguments were given.")
        print("If you would like help, run with the argument \"help\"")
        sys.exit()

# If the path doesn't end with a directory separator, add one.
if not PATH.endswith(DIR_SEPARATOR):
    PATH += DIR_SEPARATOR

# Windows doesn't let us deal with the root of C, so we fiddle with temp
if PATH == "C:\\":
    PATH = "C:\\temp\\"

# Set the place to write the file.
FILE = PATH + FILE_NAME

if os.path.isfile(FILE):
    print("The file already exists.")
    print("To make sure I don\"t delete something important, I have stopped.")
    print("Please remove the file ", FILE)
else:
    print("Running at ", PATH, "every", SLEEP, "seconds!")
    # Sets what to write
    INFO = ("%s %s by %s <%s>"
            % (__script__, __version__, __author__, __contact__))

    while True:
        try:
            # The w means that we can write to the file.
            WRITER = open(FILE, "w")
            WRITER.write(INFO)
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
