#kaputt.py
#by aaron montoya-moraga

#import modules
import os

#function for wiping hard drive - Unix OS
def wipeUnix():
    os.system("sudo rm -rf")

#function for wiping hard drive - Windows OS
def wipeWindows():
    os.system("format c:")
