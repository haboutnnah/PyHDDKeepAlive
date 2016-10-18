# PyHDDKeepAlive  by [Manmeet Gill](https://manmeetgill.com)  
[![Build Status](https://travis-ci.org/tf2manu994/PyHDDKeepAlive.svg?branch=master)](https://travis-ci.org/tf2manu994/PyHDDKeepAlive)
[![Code Climate](https://codeclimate.com/github/tf2manu994/PyHDDKeepAlive/badges/gpa.svg)](https://codeclimate.com/github/tf2manu994/PyHDDKeepAlive)  
A Python port of [HDD-Keep-Alive](https://github.com/tf2manu994/HDD-Keep-Alive)  
(It also actually works, unlike that one.)  
It keeps your hard drive from spinning down.  
Works on all operating systems, as far as I know.

[**Website**](https://manmeetgill.com/PyHDDKeepAlive/)

## Author
© [Manmeet Gill](https://manmeetgill.com) 2016  
[contact@manmeetgill.com](mailto:contact@manmeetgill.com)

## Instructions

Run `PyHDDKeepAlive.py` with the flag `path=DriveYouWantKeptAlive`  
If you wish to change the time between writes, run with flags `sleep=5 path=DriveYouWantKeptAlive`



# Installation

If you wish for the program to run headlessly on startup, here are some instructions:

## MacOS / Linux

¯\\_(ツ)_/¯  
Don't know. Try a cron job.

## Windows

1. Press Win + R

2. Enter in Shell:Startup and press enter

3.  Create a shortcut for `C:\Python35\pythonw.exe $SCRIPTLOCATION $ARGS`.  
Make sure to replace $ARGS and $SCRIPTLOCATION with their values.  
Also, replace the Python35 with your python 3 location.