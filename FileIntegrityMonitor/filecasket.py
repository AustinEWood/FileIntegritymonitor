#!/usr/bin/env python
import hashlib
import os
import time
import schedule
import logging

logging.basicConfig(filename='logfile.log', level=logging.DEBUG)

print('Thank you for using File Casket...')

#print('type check file to check a file')

#print('type clear to clear log file')

#choice = input('what would you like to do: ')

directory = "/home/kali/Documents/projects/FileIntegrityMonitor/"

FileName = input("File Name:")

Location = directory + FileName

try:
    with open(Location, "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)
            (file_hash.digest())

            print(file_hash.hexdigest())
except:
    print("File not found!")

try:
 logging.info(FileName)  # this is how I log the hash to log file
 logging.info(file_hash.hexdigest())
except:
    print("Please change file location!")


#a_file = open('logfile.log', 'w')  #this is how I clear the log file
#a_file.truncate()
#a_file.close()
